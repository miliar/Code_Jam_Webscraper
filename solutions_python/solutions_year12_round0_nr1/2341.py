#!/usr/bin/python

#dict of characters and their translations
dictionary = {
    'a' : 'y',
    'b' : 'h',
    'c' : 'e',
    'd' : 's',
    'e' : 'o',
    'f' : 'c',
    'g' : 'v',
    'h' : 'x',
    'i' : 'd',
    'j' : 'u',
    'k' : 'i',
    'l' : 'g',
    'm' : 'l',
    'n' : 'b',
    'o' : 'k',
    'p' : 'r',
    'q' : 'z',
    'r' : 't',
    's' : 'n',
    't' : 'w',
    'u' : 'j',
    'v' : 'p',
    'w' : 'f',
    'x' : 'm',
    'y' : 'a',
    'z' : 'q',
    }

#returns the translated form of a single character
def translate(character, dictionary):

    return dictionary[character]

input_file = open('A-small-attempt0.in','r')
input_lines = input_file.readlines()
input_file.close()
number_of_cases = int(input_lines.pop(0))
output = ""

for i in range(1,number_of_cases+1):
    translated_string = ''
    for char in input_lines.pop(0):
        try: newchar = translate(char, dictionary)
        except KeyError: newchar = char
        translated_string = translated_string + newchar
    output = output + 'Case #' + str(i) + ': ' + translated_string
    
output_file = open('output', 'w')
output_file.write(output)
output_file.close()
    
