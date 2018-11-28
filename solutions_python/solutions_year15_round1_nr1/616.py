__author__ = 'sarrtv'
import Queue
import numpy as np
import fileinput
import math

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
  dt=np.diff(test[::-1])

  r1=sum(max(d,0) for d in dt)

  rate=max(dt)/10.0

  r2=sum([min(d,10*rate) for d in test[0:-1]])

  return [r1, r2]


f = open('results_large.txt', 'w')
for ix, test in enumerate(tests):
    res=compute_problem(test)
    f.write('Case #%i: %i %i\n' %(ix+1, res[0], res[1]))
    print('Case #%i: %i %i\n' %(ix+1, res[0], res[1]))
f.close()
