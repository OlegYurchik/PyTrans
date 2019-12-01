import pyperclip
from translation import get_translate
import sys

if __name__ == "__main__":
    cd = pyperclip
    to_lang = sys.argv[1]
    text = cd.paste()

    output = get_translate(text=text, to_lang=to_lang, from_lang="AUTO")
    cd.copy(output)
