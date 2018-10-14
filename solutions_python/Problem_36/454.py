import re
from itertools import *

f = open('welcome.in')

lines = f.readlines()
number_of_lines = int(lines[0])
lines = lines[1:]

welcome_regex = '.*'.join([i for i in 'welcome to code jam'])
phrase = 'welcome to code jam'

#Purge unused chars
def purge_chars(x):
    return ( i for i in x if i in phrase )

def purge_before_first_w(x):
    return dropwhile(lambda q: q != 'w', x) 
    
class C(object):
    def __init__(self,f,g):
        self.f = f
        self.g = g
    def __call__(self, l):
        return self.f(self.g(l))

f = C(purge_chars, purge_before_first_w)

def line_to_dict(s):
    d = {}
    for i in range(0,len(s)):
        if s[i] not in d:
            d[s[i]] = [i]
        else:
            d[s[i]] = d[s[i]] + [i]
    return d

def golden_path(line, i, position):
    if position+1 >= len(phrase):
        if phrase[position] == 'm':
            return 1
        else:
            return 0

    current_char = line[i]

    if phrase[position+1] not in d:
        return 0

    next_char = ( next for next in d[phrase[position+1]] if next > i)
    sum = 0
    for char in next_char:
        sum += golden_path(line, char, position+1)

    return sum
        

for current_line, c in izip(lines, count(1)):
    curr_line = list(f(current_line))
    d = line_to_dict(curr_line)

    sum = 0
    if 'w' in d:
        for i in d['w']:
            sum += golden_path(curr_line,i,0)

    print "Case #%d: %04d" % (c,sum)
