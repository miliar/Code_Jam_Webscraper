#! /usr/bin/python2

import string

def main():
    a = 'abcdefghijklmnopqrstuvwxyz'
    b = 'yhesocvxduiglbkrztnwjpfmaq'
    nb_lines = int(raw_input())
    for it in xrange(nb_lines):
        line = raw_input()
        print "Case #%d: %s" % (it + 1, line.translate(string.maketrans(a, b)))

if __name__ == '__main__':
    main()
