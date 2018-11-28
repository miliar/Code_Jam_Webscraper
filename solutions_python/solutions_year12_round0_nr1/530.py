#!/usr/bin/python3

from sys import argv

mapping = { 'a': 'y', 'b': 'h', 'c': 'e', 'd': 's', 'e': 'o', 'f': 'c',
            'g': 'v', 'h': 'x', 'i': 'd', 'j': 'u', 'k': 'i', 'l': 'g',
            'm': 'l', 'n': 'b', 'o': 'k', 'p': 'r', 'q': 'z', 'r': 't',
            's': 'n', 't': 'w', 'u': 'j', 'v': 'p', 'w': 'f', 'x': 'm',
            'y': 'a', 'z': 'q', ' ': ' ' }

infile = open(argv[1])
cases = int(infile.readline())
#print(''.join(sorted(mapping.values())))
for i in range(cases):
    encrypted = infile.readline().rstrip()
    decrypted = ''.join([mapping[j] for j in encrypted])
    print('Case #{}: {}'.format(i+1, decrypted))
