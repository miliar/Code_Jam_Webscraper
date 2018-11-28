#!/usr/bin/python
import sys
encrypt_dict = {
    ' ': ' ',
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
    }
decrypt_dict = dict(zip(encrypt_dict.values(),encrypt_dict.keys()))
messages = []
cases = None

for each_line in open(sys.argv[1]):
    line = each_line.strip()
    if cases == None:
        cases = int(line)
    else:
        messages.append(line)

for case in range(cases):
    result = "Case #"+str(case+1)+": "
    for each_letter in messages[case]:
        result += decrypt_dict[each_letter]
    print result
