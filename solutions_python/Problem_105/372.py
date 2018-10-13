'''
Created on 06.05.2012

@author: alex
'''
from __future__ import print_function
import sys
from numpy.core.defchararray import isalpha

sys.stdin = open('in', 'rb')
sys.stdout = open("out2", 'w')
classes = None

def solve(row):
    global classes
    
    if not len(classes[row]):
        return [row]
    
    paths = [None] * len(classes[row])
    for i, c in enumerate(classes[row]):
        paths[i] = solve(c-1)
    cnt = 0
    ex = set()
    rn = None
    for p in paths:
        if p:
            for n in p:
                cnt += n
                rn = n
                if n not in ex:
                    ex.add(n)
                else:
                    return [n,n]
        elif row != 0 and cnt:
            return p
    if cnt:
        return [rn]
    return 0

def solve1(row):
    global classes
    
    if not len(classes[row]):
        return [row]
    paths = [None] * len(classes[row])
    pths = []
    for i, c in enumerate(classes[row]):
        paths[i] = solve1(c-1)
        if type(paths[i]).__name__ != 'bool':
            pths += paths[i]
        else:
            return True
    for s in set(list(pths)):
        if pths.count(s) >= 2:
            #print('cnt:', row, pths)
            return True

    f = [row]
    if len(pths):
        f += pths
    return f
        
T = int(raw_input())
for t in range(T):
    N = int(raw_input())
    classes = [None] * N
    for i in range(N):
        st = [int(x) for x in raw_input().split()]
        inheritanceCount = st.pop(0)
        classes[i] = st[:inheritanceCount]
    
    #
    k = ["No", "Yes"]
    for i in range(N):
        r = solve1(i)
        if type(r).__name__ == 'bool':
            print("Case #%d: Yes" % (t+1))
            break
    else:
        print("Case #%d: No" % (t+1))
sys.stdout.close()