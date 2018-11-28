import sys

num_cases = int(sys.stdin.readline())

cases = sys.stdin.readlines()

if num_cases != len(cases):
    raise Exception("num of cases don't match");

def get_state(n, k):
    
    if (k == 0) or ((k+1) % (2**n)):
        return 'OFF'
    else:
        return 'ON'

i = 1

for case in cases:
    n, k = [int(e) for e in case.split()]
    print "Case #%s: %s" % (i, get_state(n, k))
    i += 1

