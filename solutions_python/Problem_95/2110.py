'''
Created on 14/04/2012

@author: Rachum
'''

translate = {
    'a': 'y',
    'b': 'n',
    'c': 'f',
    'd': 'i',
    'e': 'c',
    'f': 'w',
    'g': 'l',
    'h': 'b',
    'i': 'k',
    'j': 'u',
    'k': 'o',
    'l': 'm',
    'm': 'x',
    'n': 's',
    'o': 'e',
    'p': 'v',
    'q': 'z',
    'r': 'p',
    's': 'd',
    't': 'r',
    'u': 'j',
    'v': 'g',
    'w': 't',
    'x': 'h',
    'y': 'a',
    'z': 'q',
    ' ': ' '
}

translate = {translate[key] : key for key in translate}

with open('A-small-attempt0.in', 'rt') as inputfile, open('output.txt', 'wt') as outputfile:
    num_of_testcases = int(inputfile.readline())
    for i, line in enumerate(inputfile.readlines()):
        line = line.replace('\n', '')
        result = ''.join([translate[char] for char in line])
        if not i == 0:
            print(file=outputfile)
        print("Case #%d: %s" % (i+1, result), file=outputfile, end="")




    