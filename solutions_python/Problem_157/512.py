from sys import stdin
import re
import operator
import bisect
import sys
import random

quater = {
"i*": "i",
"j*": "j",
"k*": "k",

"*i": "i",
"*j": "j",
"*k": "k",

"11": "1",
"1i": "i",
"1j": "j",
"1k": "k",

"i1": "i",
"ii": "1",
"ij": "k",
"ik": "j",

"j1": "j",
"ji": "k",
"jj": "1",
"jk": "i",

"k1": "k",
"ki": "j",
"kj": "i",
"kk": "1",
}

minus = set(["ii", "ik", "ji", "jj", "kj", "kk"])

cases = int(stdin.next().strip())
for case in range(1, cases+1):
    L, X = map(int, stdin.next().split())
    my_str = stdin.next().strip()
    my_str = my_str * X

    where_i = []
    cur_char = "*"
    in_minus = False
    for i, c in enumerate(my_str):
    	trans = cur_char + c
    	if trans in minus:
    		in_minus = not in_minus
    	cur_char = quater[trans]
    	if cur_char == "i" and not in_minus:
    		where_i.append(i)

    where_k = set([])
    cur_char = "*"
    in_minus = False
    for i in range(len(my_str)-1, -1, -1):
    	c = my_str[i]
    	trans = c + cur_char
    	if trans in minus:
    		in_minus = not in_minus
    	cur_char = quater[trans]
    	if cur_char == "k" and not in_minus:
    		where_k.add(i)

    can_write = "NO"

    for start in where_i:
	    cur_char = "*"
	    in_minus = False
	    for i in range(start + 1, len(my_str)):
	    	c = my_str[i]
	    	trans = cur_char + c
	    	if trans in minus:
	    		in_minus = not in_minus
	    	cur_char = quater[trans]
	    	if cur_char == "j" and not in_minus and i+1 in where_k:
	    		can_write = "YES"
	    		break
	    if can_write == "YES":
	    	break

    print 'Case #%d: %s' % (case, can_write)