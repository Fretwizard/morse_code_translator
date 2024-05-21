MORSE_CODE_DICT = {
    'A': '.-',    'B': '-...',   'C': '-.-.',  'D': '-..',   'E': '.',
    'F': '..-.',   'G': '--.',    'H': '....',   'I': '..',    'J': '.---',
    'K': '-.-',    'L': '.-..',   'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',    'S': '...',   'T': '-',
    'U': '..-',    'V': '...-',   'W': '.--',   'X': '-..-',  'Y': '-.--',
    'Z': '--..',   '1': '.----',  '2': '..---', '3': '...--',
    '4': '....-',  '5': '.....',  '6': '-....', '7': '--...',
    '8': '---..',  '9': '----.', '0': '-----', ' ': '/'
}

# Reverse the dictionary for Morse to Text translation
REVERSE_MORSE_CODE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}

def text_to_morse(text):
    morse = ""
    for char in text.upper():  # Convert to uppercase for consistency
        if char != ' ':
            morse += MORSE_CODE_DICT.get(char, '') + ' '  # Handle invalid characters
        else:
            morse += '/ '  # Add slash for word separation
    return morse.strip()  # Remove trailing space

def morse_to_text(morse):
    text = ""
    for code in morse.split(' '):
        text += REVERSE_MORSE_CODE_DICT.get(code, '')  # Handle invalid Morse code
    return text

while True:
    choice = input("Enter 't' for text to Morse, 'm' for Morse to text, or 'q' to quit: ")

    if choice == 't':
        text = input("Enter text to translate: ")
        print(text_to_morse(text))
    elif choice == 'm':
        morse = input("Enter Morse code to translate: ")
        print(morse_to_text(morse))
    elif choice == 'q':
        break
    else:
        print("Invalid choice.")