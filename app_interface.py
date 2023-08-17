import pytesseract
from PIL import Image

import gradio as gr

def tesseract_ocr(filepath, languages):
    image = Image.open(filepath)
    return pytesseract.image_to_string(image=image, lang=', '.join(languages))

title = "Tesseract OCR"
description = "Gradio demo for Tesseract. Tesseract is an open source text recognition (OCR) Engine."
article = "<p style='text-align: center'><a href='https://tesseract-ocr.github.io/' target='_blank'>Tesseract documentation</a> | <a href='https://github.com/tesseract-ocr/tesseract' target='_blank'>Github Repo</a></p>"
examples = [
        ['examples/eurotext.png', ['eng']], 
        ['examples/tesseract_sample.png', ['jpn', 'eng']], 
        ['examples/chi.jpg', ['HanS', 'HanT']]
    ]

choices = pytesseract.get_languages()

demo = gr.Interface(
    fn=tesseract_ocr, 
    inputs=[
        gr.Image(type="filepath", label="Input"), 
        gr.CheckboxGroup(choices*40, type="value", value=['eng'], label='language')
        ],
    outputs='text',
    title=title,
    description=description,
    article=article,
    examples=examples,
)

if __name__ == '__main__':
    demo.launch(server_port=7861, enable_queue=True)
