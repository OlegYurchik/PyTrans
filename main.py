import pyperclip
from translation import get_translate
import sys

cd = pyperclip

to_lang = sys.argv[1]


text = cd.paste()

try:
    output = get_translate(text=text, to_lang=to_lang, from_lang="AUTO")
    cd.copy(output)
except Exception:
    print("Sorry, try again")