"""
Filename: googlerese.py
Author: Jason Cramer

This program is intended to translate strings of text form Googlerese to
English. The input first takes in the number of strings to be translated,
followed by the strings to be translated, separated by newline characters.
The input is taken in on the command line.

"""


from sys import exit


# The translation dictionary from Googlerese to English
translationDict = {'y':'a', 'n':'b', 'f':'c', 'i':'d', 'c':'e', 'w':'f', 'l':'g', 'b':'h', 'k':'i', 'u':'j', 'o':'k', 'm':'l', 'x':'m', 's':'n', 'e':'o', 'v':'p', 'z':'q', 'p':'r', 'd':'s', 'r':'t', 'j':'u', 'g':'v', 't':'w', 'h':'x', 'a':'y', 'q':'z', ' ':' ', '\n':'\n'}

def translate(sentence):
    """ Translates a string from Googlerese to English, returning the translated
        string. """

    translated = ''
    for c in sentence:
        translated += translationDict[c]
    return translated

def main():
    f = open('output.txt', '+w')
    for i in range(int(input())):
        f.write('Case #' + str(i + 1) + ': ' + translate(input()) + '\n')


if __name__ == '__main__':
    exit(main())
    


