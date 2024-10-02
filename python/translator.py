import sys


braille_to_char = {
    '.....O': 'capital',
    '.O...O': 'decimal',
    '.O.OOO': 'number',

    'O.....': 'a',  'O.O...': 'b',  'OO....': 'c',  'OO.O..': 'd',  'O..O..': 'e',
    'OOO...': 'f',  'OOOO..': 'g',  'O.OO..': 'h',  '.OO...': 'i',  '.OOO..': 'j',
    'O...O.': 'k',  'O.O.O.': 'l',  'OO..O.': 'm',  'OO.OO.': 'n',  'O..OO.': 'o',
    'OOO.O.': 'p',  'OOOOO.': 'q',  'O.OOO.': 'r',  '.OO.O.': 's',  '.OOOO.': 't',
    'O...OO': 'u',  'O.O.OO': 'v',  '.OOO.O': 'w',  'OO..OO': 'x',  'OO.OO.': 'y',
    'O..OOO': 'z',

    '......': ' '
}
braille_to_symbol={ '..OO.O': '.',  '..O...': ',',  '..O.OO': '?',  '..OOO.': '!',
    '....OO': ':',  '..O.O.': ';',  '....OO': '-',  '.O..O.': '/',  '.OO..O': '<',
    'O..OO.': '>',  'O.O..O': '(',  '.O.OO.': ')'
    }
braille_to_number = {
    'O.....': '1',  'O.O...': '2',  'OO....': '3',  'OO.O..': '4',  'O..O..': '5',
    'OOO...': '6',  'OOOO..': '7',  'O.OO..': '8',  '.OO...': '9',  '.OOO..': '0',
}
# When a Braille capital follows symbol is read, assume only the next symbol should be capitalized.
# When a Braille number follows symbol is read, assume all following symbols are numbers until the next space symbol.
char_to_braille = {value: key for key, value in braille_to_char.items()}
number_to_braille = {value: key for key, value in braille_to_number.items()}


def translate(char):

    if ".O" in char or "O." in char:
        print(convert_braille_to_char(char))
    else:
        print(convert_char_to_braille(char))

def convert_braille_to_char(braille):
    capitalize = False
    isnumber = False
    answer=""

    braillelist = [braille[i:i+6] for i in range(0, len(braille), 6)]

    for i in braillelist:
        if i in braille_to_char:
            if braille_to_char[i] == "capital":
                capitalize = True
                continue
            elif braille_to_char[i] == "number":
                isnumber = True
                continue
            elif braille_to_char[i] == " ":
                isnumber = False 
                answer += " "
                continue

            if capitalize and isnumber==False:
                answer += braille_to_char[i].upper()
                capitalize=False
            elif isnumber and i in braille_to_number:
                answer += braille_to_number[i]
            else:
                answer += braille_to_char[i]
            
       
    
    return answer

def convert_char_to_braille(char):
    isnumber = False
    answer=""

    charlsit = list(char)

    for i in charlsit:
        if i.isupper():
            answer+=char_to_braille['capital']
        if i.lower() in char_to_braille:
           
            if i ==' ':
                isnumber=False
            answer+=char_to_braille[i.lower()]
            continue
        if i in number_to_braille:
            if not isnumber:
                answer+=char_to_braille['number']
                isnumber = True
            answer+=number_to_braille[i]
            continue
    
    return answer

if __name__ == "__main__":
   

    # Join the arguments to form the input string
    input_text = ' '.join(sys.argv[1:])  # This combines all arguments after the script name
    translate(input_text)
