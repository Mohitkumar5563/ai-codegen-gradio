
from model_loader import load_model
import gradio as gr

codegen = load_model()

def generate_code(prompt):
    response = codegen(prompt, max_length=100, do_sample=True, temperature=0.7)
    return response[0]['generated_text']

iface = gr.Interface(fn=generate_code, inputs="text", outputs="text", title="AI Code Generator")
iface.launch()
