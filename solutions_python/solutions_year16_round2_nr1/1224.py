"""
ZERO : Z
ONE : 
TWO : W
THREE : 
FOUR : U
FIVE : 
SIX : X
SEVEN : 
EIGHT : G
NINE :


ONE : O
THREE : H
FIVE : F
SEVEN : 
NINE :

SEVEN : V
NINE : I

"""

#Order: ZERO, TWO, FOUR, SIX, EIGHT, ONE, THREE, FIVE, SEVEN, NINE

from collections import Counter

def digits(s):
    output = []
    count = Counter(s.lower())

    while count['z']:
        output.append(0)
        count['z'] -= 1
        count['e'] -= 1
        count['r'] -= 1
        count['o'] -= 1

    while count['w']:
        output.append(2)
        count['t'] -= 1
        count['w'] -= 1
        count['o'] -= 1        

    while count['u']:
        output.append(4)
        count['f'] -= 1
        count['o'] -= 1
        count['u'] -= 1
        count['r'] -= 1

    while count['x']:
        output.append(6)
        count['s'] -= 1
        count['i'] -= 1
        count['x'] -= 1


    while count['g']:
        output.append(8)
        count['e'] -= 1
        count['i'] -= 1
        count['g'] -= 1
        count['h'] -= 1
        count['t'] -= 1


    while count['o']:
        output.append(1)
        count['o'] -= 1
        count['n'] -= 1
        count['e'] -= 1
        

    while count['h']:
        output.append(3)
        count['t'] -= 1
        count['h'] -= 1
        count['r'] -= 1
        count['e'] -= 2


    while count['f']:
        output.append(5)
        count['f'] -= 1
        count['i'] -= 1
        count['v'] -= 1
        count['e'] -= 1


    while count['v']:
        output.append(7)
        count['s'] -= 1
        count['v'] -= 1
        count['n'] -= 1
        count['e'] -= 2


    while count['i']:
        output.append(9)
        count['i'] -= 1
        count['n'] -= 2
        count['e'] -= 1

    return "".join([str(i) for i in sorted(output)])
        
        
t = int(raw_input())  # read a line with a single integer

for i in xrange(1, t + 1):
  s = raw_input()
  print "Case #{}: {}".format(i, digits(s))
