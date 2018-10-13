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
... 4 O 2 B 1 B 2 O 4
... 3 O 5 O 8 B 100
... 2 B 2 B 1
... ''')  #doctest: +NORMALIZE_WHITESPACE
Case #1: 6
Case #2: 100
Case #3: 4

"""
__docformat__ = 'restructuredtext en'

from codejam import *

def solve(line):
    loc = dict(O=(1, 0), B=(1, 0)) # where, when
    T = 0
    for item in line:
        if item in 'OB':
            bot = item
        else:
            button = int(item)
            dist = abs(loc[bot][0] - button) - (T - loc[bot][1])
            T += (dist > 0 and dist + 1 or 1)
            loc[bot] = (button, T)
    return T

def parse(fi):
    line = fi.next().split()
    N = int(line[0])
    assert len(line) == 2 * N + 1
    line.pop(0)
    return line,

def format(r):
    return r

if __name__ == '__main__':
    main(solve, parse, format)
