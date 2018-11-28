from math import *
import sys

def create_state(n):
    def state(k):
        if k == 0:
            return "0"+n*"."+"0"
        else:
            prev_state = state(k-1)
            lower = prev_state.find(max(prev_state.split("0")))
            upper = lower + len(max(prev_state.split("0")))
            pos = int(floor((lower + upper - 1) / 2.0))
            return prev_state[0:pos]+"0"+prev_state[pos+1:]
    return state

sys.setrecursionlimit(100000)
t = int(raw_input())
for i in xrange(1, t + 1):
    n, k = [int(s) for s in raw_input().split(" ")]
    state = create_state(n)
    d = len(max(state(k-1).split("0")))
    if d % 2 == 0:
        a = int(floor((d - 1) / 2.0))
        b = int(ceil((d - 1)/ 2.0))
    else:
        a = b = (d - 1) / 2 
    print "Case #{}: {} {}".format(i,b,a)
        

