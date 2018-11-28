#!/usr/bin/env python
from string import maketrans 

_in  = 'abcdefghijklmnopqrstuvwxyz' 
_out = 'yhesocvxduiglbkrztnwjpfmaq'

tab = maketrans(_in, _out)

_input = open('input')
i = int(_input.readline())
lines = 0

for i in range(i):
    lines += 1
    line = _input.readline()[:-1].translate(tab);
    print 'Case #%s:' % lines, line
