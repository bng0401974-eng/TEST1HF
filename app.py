import gradio as gr


def test_function(ime):
    return f"🚀 Zdravo {ime}! Serverot raboti uspesno."


# Praveme ednostaven interfejs
with gr.Blocks() as demo:
    gr.Markdown("# LATIVM TEST")
    ime_input = gr.Textbox(label="Vnesi tvoe ime")
    kopce = gr.Button("Test")
    izlez = gr.Textbox(label="Status")

    kopce.click(fn=test_function, inputs=ime_input, outputs=izlez)

if __name__ == "__main__":
    demo.launch()