from string import maketrans
import sys

source = 'abcdefghijklmnopqrstuvwxyz'
dest   = 'ynficwlbkuomxsevzpdrjgthaq'

transtab = maketrans(dest, source)

if __name__ == '__main__':
    n = int(raw_input())
    for i in xrange(n):
        string = raw_input()
        print 'Case #%d: %s' % (i+1, string.translate(transtab))
