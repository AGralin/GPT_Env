# chatgpt-retrieval

Simple script to use ChatGPT on your own files.

[YouTube Video](https://youtu.be/9AXP7tCI9PI).

## Installation

Install [Langchain](https://github.com/hwchase17/langchain) and other required packages.
```
pip install langchain openai chromadb tiktoken unstructured
```
Modify `.env` to use your own [OpenAI API key](https://platform.openai.com/account/api-keys)
- Ensure you have enough API credits

Place your own data into `data/data.txt`.

## Example usage
Test reading `data/data.txt` file.
> python simpleGPT.py "what is alpha"