# Text to morse code converter

print("Text to Morse Converter")

morse_dict = {'A': '.-', 'B': '-...',
              'C': '-.-.', 'D': '-..', 'E': '.',
              'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-',
              'L': '.-..', 'M': '--', 'N': '-.',
              'O': '---', 'P': '.--.', 'Q': '--.-',
              'R': '.-.', 'S': '...', 'T': '-',
              'U': '..-', 'V': '...-', 'W': '.--',
              'X': '-..-', 'Y': '-.--', 'Z': '--..',
              '1': '.----', '2': '..---', '3': '...--',
              '4': '....-', '5': '.....', '6': '-....',
              '7': '--...', '8': '---..', '9': '----.',
              '0': '-----', ',': '--..--', '.': '.-.-.-',
              '?': '..--..', '/': '-..-.', '-': '-....-',
              '(': '-.--.', ')': '-.--.-', "'": '. _ _ _ _ .', '"': '. _ . . _ .',
              ';': '_ . _ . _ .', '_': '. . _ _ . _', '+': '. _ . _ .', '*': '_ . . _', '@': '	. _ _ . _ .',
              }


def encoder(sentence):
    final_text = ""
    for char in sentence:
        if char == " ":
            final_text += char
            continue
        elif char not in morse_dict:
            print(f'character {char} is invalid. Please enter different character.')
            return
        word = morse_dict[char]
        final_text += word
    print(f'Encoded text: {final_text}')
    return


# Get the input from the user
text = input("Enter the text to convert\t")
encoder(text.upper())
print('Program Ended!')
