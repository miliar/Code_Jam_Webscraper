#-*- coding:utf-8 -*-
#!/usr/bin/env/python
def readInt(): return int(raw_input())
def readArray(num_):
    result = []
    for i in xrange(num_):
        result.append(raw_input())
    return result
def readLineArray(func_): return map(func_,raw_input().split())

def nextQueue(current_,max_):
    passenger = 0
    for i in range(len(current_)):
        passenger += current_[i]
        if passenger > max_:
            passenger -= current_[i]
            break
    return (current_[i:]+current_[:i],passenger)

T = readInt()
for i in range(T):
    (R,k,N) = readLineArray(int)
    groups  = readLineArray(int)
    result = 0
    for j in range(R):
        (groups,earn) = nextQueue(groups,k)        
        result += earn
    print "Case #%d: %d" %(i+1,result)

