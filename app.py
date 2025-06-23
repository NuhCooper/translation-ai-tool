from transformers import MarianMTModel, MarianTokenizer
import gradio as gr

# Map translation directions to pre-trained MarianMT models
lang_map = {
    "English to French": "Helsinki-NLP/opus-mt-en-fr",
    "English to German": "Helsinki-NLP/opus-mt-en-de",
    "English to Spanish": "Helsinki-NLP/opus-mt-en-es",
    "English to Italian": "Helsinki-NLP/opus-mt-en-it",
    "English to Dutch": "Helsinki-NLP/opus-mt-en-nl",
    "English to Portuguese": "Helsinki-NLP/opus-mt-en-pt",
    "English to Polish": "Helsinki-NLP/opus-mt-en-pl",
    "English to Chinese": "Helsinki-NLP/opus-mt-en-zh",
    "English to Japanese": "Helsinki-NLP/opus-mt-en-ja",
    "English to Arabic": "Helsinki-NLP/opus-mt-en-ar"
}

# Translation function
def translate(text, direction):
    model_name = lang_map[direction]
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)

    tokens = tokenizer(text, return_tensors="pt", padding=True)
    output = model.generate(**tokens)
    result = tokenizer.decode(output[0], skip_special_tokens=True)
    return result

# Create Gradio interface
interface = gr.Interface(
    fn=translate,
    inputs=[
        gr.Textbox(label="Enter your survey question"),
        gr.Dropdown(choices=list(lang_map.keys()), label="Translate to")
    ],
    outputs="text",
    title="Survey Translation Tool",
    description="Use AI to translate survey questions quickly and accurately!"
)

# Run the app
if __name__ == "__main__":
    interface.launch()
