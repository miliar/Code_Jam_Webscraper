""" Welcome to Code Jam

:Abstract: Solution to Google Code Jam 2011 qualification
:Authors:  iki
:Contact:  jan.killian at (g)mail.com

.. contents::

Problem statement
=================

Input
-----

Output
------

Limits
------

Doctest
=======

>>> test(
...   testlabel='sample via parse()',
...   testinput='''3
... 2 3
... ###
... ###
... 1 1
... .
... 4 5
... .##..
... .####
... .####
... .##..
... ''')  #doctest: +NORMALIZE_WHITESPACE
Case #1:
Impossible
Case #2:
.
Case #3:
./\\..
.\\//\\
./\\\\/
.\\/..
"""
__docformat__ = 'restructuredtext en'

from codejam import *

def solve(R, C, I):
    if log.debug: log.debug([R, C, I[0]])
    for r in xrange(R):
        for c in xrange(C):
            if I[r][c] == '#':
                if log.debug: log.debug([r, c])
                if c+1 >= C or r+1 >= R:
                    return False
                elif '#' == I[r][c+1] == I[r+1][c] == I[r+1][c+1]:
                    I[r][c] = I[r+1][c+1] = '/'
                    I[r][c+1] = I[r+1][c] = '\\'
                else:
                    return False
    return I

def parse(fi):
    R, C = map(int, fi.next().split())
    return R, C, [ list(fi.next().strip()) for line in xrange(R) ]

def format(r):
    return r and ('\n%s' % '\n'.join(''.join(row) for row in r)) or '\nImpossible'

if __name__ == '__main__':
    main(solve, parse, format)
