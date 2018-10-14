__author__ = 'sarrtv'
import Queue
import numpy as np
import fileinput

lines=list(fileinput.input())

n_test_cases=int(lines[0])

tests=[]
for i in range(1,len(lines),2):
    d=int(lines[i])
    testLine=lines[i+1]
    ds=testLine.split()
    tests.append([int(di) for di in ds])

assert(len(tests)==n_test_cases)


def compute_problem(test):
    totalTime=0
    q=Queue.Queue()
    q.put({"problem":test, "t": 0})

    while not q.empty():
        cur=q.get()
        #print cur

        if sum(cur["problem"])==0:
            totalTime=cur["t"]
            break
        else:
            q.put(decreateEveryOne(cur))
            q.put(redistribute(cur,2))
            q.put(redistribute(cur,3))

    return totalTime

def decreateEveryOne(test):
    result={"problem":[max(t-1,0) for t in test["problem"]], "t":test["t"]+1}
    return result

def redistribute(test, k):
    result={"problem": None, "t":test["t"]+1}
    test2=[i for i in test["problem"]]
    offThePlate=max(test2)/k
    maxIdx=test2.index(max(test2))

    test2[maxIdx]=test2[maxIdx]-offThePlate
    test2.append(offThePlate)

    result["problem"]=test2

    return result

f = open('results_small2.txt', 'w')
for ix, test in enumerate(tests):
    f.write('Case #%i: %i\n' %(ix+1, compute_problem(test)))
f.close()
