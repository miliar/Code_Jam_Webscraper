# -*- coding: utf-8 -*-

import string, itertools, re


alphabet = set(string.ascii_lowercase)

D = {'a': 'y',
 'b': 'h',
 'c': 'e',
 'd': 's',
 'e': 'o',
 'f': 'c',
 'g': 'v',
 'h': 'x',
 'i': 'd',
 'j': 'u',
 'k': 'i',
 'l': 'g',
 'm': 'l',
 'n': 'b',
 'o': 'k',
 'p': 'r',
 'q': 'z',
 'r': 't',
 's': 'n',
 't': 'w',
 'u': 'j',
 'v': 'p',
 'w': 'f',
 'x': 'm',
 'y': 'a',
 'z': 'q'}



def generate_strings(s):
    return ''.join(D[i] if i in alphabet else i for i in s)

patt = re.compile('Case #\d+: ')

with open('A-small-attempt0.in') as f, open ('out.txt','w') as f_out:
    f.__next__()
    
    for i,line in enumerate(f,1):
        line = line.rstrip()
        line = generate_strings(line)
        print(line)
        f_out.write('Case #{}: {}\n'.format(i,line))
        
        



