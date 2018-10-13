numbers = []
def number_func(n, A, B):
    r = 0
    nl = list(str(n))
    for i in range(len(nl)-1):
        ns = nl.pop(0)
        nl.append(ns)
        nt = int(string.join(nl, ''))
        if A<nt and nt<=B and nt!=n and n<nt and nl[0]!=0:
            numbers.append(nt)
            #print "(", n, ",", nt, ")"
            #print "1"
            r += 1
        #else:
            #print ""
    #if r>0:
        #numbers.append(n)
    return r

def main(A, B):
    r = 0
    if B>=10:
        for n in range(A, B):
            r += number_func(n, A, B)
    numbers.sort()
    #print numbers
    return r

import string
import sys
T = int(sys.stdin.readline())
for i in range(T):
    line = str(sys.stdin.readline())
    line = string.split(line, " ")
    print "Case #%d:" % (i + 1),
    A = line.pop(0)
    B = line.pop(0)
    res = main(int(A), int(B))
    print res
    numbers = []
    #for s in res:
    #    print '"%s"' % s if s is not None else ':('
"""
4
1 9
10 40
100 500
1111 2222

1
10 40

1
1111 2222

1
11 22

"""