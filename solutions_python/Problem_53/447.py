#-*- coding:utf-8 -*-
#!/usr/bin/env/python
def readInt(): return int(raw_input())
def readArray(num_):
    result = []
    for i in xrange(num_):
        result.append(raw_input())
    return result
def readLineArray(func_): return map(func_,raw_input().split())

T = readInt()
for i in range(T):
    (N,K) = readLineArray(int)
    snappers = [False] * N
    for j in range(K):
        poweron = True
        for k in range(len(snappers)):
            snappers[k] = not(snappers[k])
            if snappers[k]:
                break
    print "Case #%d: %s" %(i+1,"ON" if all(snappers) else "OFF")

