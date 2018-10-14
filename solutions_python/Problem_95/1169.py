#!/usr/bin/python -tt

import sys

def create_dict():
    dico = {'y':'a', 'e':'o', 'q':'z', 'z':'q'}
    crypted = ['ejp mysljylc kd kxveddknmc re jsicpdrysi',
               'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
               'de kr kd eoya kw aej tysr re ujdr lkgc jv']
    clear = ['our language is impossible to understand',
             'there are twenty six factorial possibilities',
             'so it is okay if you want to just give up']
    for i, sentence in enumerate(crypted):
        for j, letter in enumerate(sentence):
            if letter != ' ':
                if dico.has_key(letter):
                    assert dico[letter] == clear[i][j]
                else:
                    dico[letter] = clear[i][j]
    return dico

def parse_case(input_file):
    with open(input_file) as f:
        n_test_cases = int(f.readline())
        cases = []
        for case in xrange(n_test_cases):
            cases.append(f.readline().strip())
    return cases

def translate(case, dico):
    output = ''
    for letter in case:
        if dico.has_key(letter):
            output += dico[letter]
        else:
            output += letter
    return output

def main():
    if len(sys.argv) != 2:
        sys.exit(1)
    dico = create_dict()
    cases = parse_case(sys.argv[1])
    i = 0
    for case in cases:
        i += 1
        print 'Case #%d: %s' % (i, translate(case, dico))

if __name__ == '__main__':
    sys.exit(main())


