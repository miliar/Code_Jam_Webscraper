
f = open('alien.in')
lines = f.readlines()
first_line = lines[0]
lines = lines[1:]
L, D, N = tuple([int(num) for num in first_line.split(' ')])

plain_text = lines[0:D]
regex = lines[D:D+N]

#print L, D, N
#print plain_text
#print regex

import re
from itertools import *

def par_to_cor(p):
    s = re.sub('\(','[', p)
    s = re.sub('\)', ']',s)
    return s

tuned_regex = [par_to_cor(p) for p in regex]
regex_count = count(1)
for i in [ (regex_count.next(), sum([ 1 for text in plain_text if re.match(regex,text)])) for regex in tuned_regex]:
    print 'Case #%i: %i' % i
