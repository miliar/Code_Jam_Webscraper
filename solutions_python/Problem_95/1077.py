#! /opt/local/bin/python
# -*- coding: utf8 -*-

DICTIONARY = {
'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm',
'q': 'z', 'z': 'q'
}


def main():
    dict = {}
    for c in range(input()):
        str_in = raw_input()
        str_out = ''
        for i in range(len(str_in)):
            if DICTIONARY.has_key(str_in[i]):
                str_out += DICTIONARY[str_in[i]]
            else:
                str_out += str_in[i]
        print 'Case #%d: %s' % ( c+1, str_out )
   

if __name__ == '__main__':
    main()
