#!/usr/bin/env python

import math

# f = open('sample.in', 'r')
f = open('C-small-attempt0.in', 'r')

def check_palindrome(s):
    if len(s) > 1:
        if s == s[::-1]:
            return True
    else:
        return True
    return False

def check_square(x):
    a = math.floor(math.sqrt(x))
    if a*a == x:
        return int(a)
    return False

row = 0
out = ''
for line in f:
    if row == 0:
        row +=1
        continue

    start   = int(line.split(' ')[0])
    end     = int(line.split(' ')[1])
    tot     = 0

    for x in xrange(start, end+1):
        # check palindrome
        pq  = False
        p   = check_palindrome(str(x))

        if p == True:
            # check square and palindrome
            sq = check_square(x)
            pq = check_palindrome(str(sq))

        if pq:
            tot += 1

    out += 'Case #%i: %i\n' % (row, tot)
    row +=1

f.close()

with open ('output', 'w') as f: 
    f.write (out)
