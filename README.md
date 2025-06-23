---
title: survey-translation-ai-tool
emoji: 🌍
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: 5.31.0
app_file: app.py
pinned: false
---


# Survey Translation AI Tool

This project provides a simple, lightweight AI-powered solution for translating short survey questions into multiple languages. It demonstrates how pre-trained neural machine translation models can support faster localisation workflows in a business context.

## Features

 - Uses Hugging Face MarianMT models for neural machine translation (NMT)

 - Supports multiple language pairs (e.g., English to French, German, Spanish)

 - Simple, interactive user interface built with Gradio

 - Deployable as a public web app on Hugging Face Spaces

 - Designed for quick extension with additional languages as needed

## File Structure

 - app.py - Contains the Gradio app logic and translation pipeline.

 - requirements.txt - Lists the Python dependencies.

 - README.md - Project overview and usage instructions.

## How to Run Locally

1. Clone this repository:
```
git clone https://github.com/NuhCooper/translation-ai-tool.git
cd translation-ai-tool
```
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Launch the app:
```
python app.py
```
## Deployment

This tool is structured for one-click deployment on Hugging Face Spaces. Simply connect this repository when creating a new Space and select Gradio as the SDK.

## License

This project is provided under the MIT License.

## Author

Nuh Cooper
