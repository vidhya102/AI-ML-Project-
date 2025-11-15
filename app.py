import gradio as gr

def greet(name):(venv) 

    return f"Hello {name}! Welcome to AI/ML Demo 😊"

demo = gr.Interface(
    fn=greet,
    inputs="text",
    outputs="text",
    title="AI/ML Model Demo App",
    description="Type your name to see a demo response."
)

demo.launch()
