from config import *
import docraptor
from flask import Flask, render_template, jsonify

application = Flask(__name__)
application.config['SECRET_KEY'] = 'whatever-you-do-dont-tell-anyone'

docraptor.configuration.username = DOC_RAPTOR_API_KEY
doc_api = docraptor.DocApi()


@application.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html", canvas_drawing=CANVAS_DRAWING)


@application.route("/generate_pdf", methods=["POST", "GET"])
def generate_pdf():
    print("pdf conversion process started")
    pdf_template = render_template("index.html", canvas_drawing=CANVAS_DRAWING)
    pdf_file = doc_api.create_doc({
      "test": True,
      "document_content": pdf_template,
      "name": "test-repo.pdf",
      "document_type": "pdf",
      "javascript": True,
    })
    print("pdf conversion process finished")
    return jsonify(status='pdf successfully converted!')


if __name__ == '__main__':
    application.debug = True
    application.run()
