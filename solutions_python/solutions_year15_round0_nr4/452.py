from sys import stdin
import re
import operator
import bisect
import sys
import random

cases = int(stdin.next().strip())
for case in range(1, cases+1):
    X, R, C = map(int, stdin.next().split())
    R, C = min(R,C), max(R,C)
    S = R*C
    who_wins = "RICHARD"
    if S % X == 0:
    	if X == 1 or X == 2:
    		who_wins = "GABRIEL"
    	if X == 3 and R > 1:
    		who_wins = "GABRIEL"
    	if X == 4 and R > 2:
    		who_wins = "GABRIEL"
    print 'Case #%d: %s' % (case, who_wins)