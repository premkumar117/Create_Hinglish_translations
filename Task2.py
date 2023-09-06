from translate import Translator

# Function to translate English to Hinglish
def translate_to_hinglish(text):
    try:
        translator = Translator(to_lang="hi")
        hinglish_text = translator.translate(text)
        return hinglish_text

    except Exception as e:
        return str(e)

# Test the translation function with your sample statements
statements = [
    "Definitely share your feedback in the comment section.",
    "So even if it's a big video, I will clearly mention all the products.",
    "I was waiting for my bag."
]

for statement in statements:
    hinglish_statement = translate_to_hinglish(statement)
    print(f"Statement: {statement}")
    print(f"Output: {hinglish_statement}\n")


