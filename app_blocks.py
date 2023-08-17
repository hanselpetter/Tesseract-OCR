import gradio as gr
import pytesseract
from PIL import Image

def tesseract_ocr(filepath, languages):
    image = Image.open(filepath)
    return pytesseract.image_to_string(image=image, lang=', '.join(languages) if languages else None)

title = "Tesseract OCR"
description = "Gradio demo for Tesseract. Tesseract is an open source text recognition (OCR) Engine."
article = "<p style='text-align: center'><a href='https://tesseract-ocr.github.io/' target='_blank'>Tesseract documentation</a> | <a href='https://github.com/tesseract-ocr/tesseract' target='_blank'>Github Repo</a></p>"
examples = [
    ["examples/eurotext.png", ["eng"]],
    ["examples/tesseract_sample.png", ["jpn", "eng"]],
    ["examples/chi.jpg", ["HanS", "HanT"]],
]

with gr.Blocks(title=title) as demo:
    gr.Markdown(f'<h1 style="text-align: center; margin-bottom: 1rem;">{title}</h1>')
    gr.Markdown(description)
    with gr.Row():
        with gr.Column():
            image = gr.Image(type="filepath", label="Input")
            choices = pytesseract.get_languages()
            with gr.Accordion("Languages", open=False):
                languages = gr.CheckboxGroup(choices*40, type="value", value=["eng"], label='language')
            with gr.Row():
                btn_clear = gr.ClearButton([image, languages])
                btn_submit = gr.Button(value="Submit", variant="primary")
        with gr.Column():
            text = gr.Textbox(label="Output")

    btn_submit.click(tesseract_ocr, inputs=[image, languages], outputs=text)
    btn_clear.add(text)

    gr.Examples(
        examples=examples,
        inputs=[image, languages],
    )

    gr.Markdown(article)

if __name__ == '__main__':
    demo.launch()
