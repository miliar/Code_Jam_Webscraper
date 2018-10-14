#!/usr/bin/python
# -*- coding: utf-8 -*-

from sys import stdin

if __name__ == "__main__":

    translation_table = {
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
        ' ' : ' ',
        '\n': ''
    }


    n = int(stdin.readline())
    casen = 1

    while True:
        text = stdin.readline()
        if not text:
            break
        new_text = ''.join(map(lambda ch: translation_table[ch], text))
        print  'Case #' + str(casen) + ': ' + new_text 
        casen += 1

