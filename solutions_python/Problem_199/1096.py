# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
'''
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
  print "Case #{}: {} {}".format(i, n + m, n * m)
  # check out .format's specification for more formatting options
'''
import time
#t0=time.clock()

t = int(raw_input())  # read a line with a single integer
for tr in xrange(1, t + 1):
    plminstate, k = [s for s in raw_input().split(" ")]
    k=int(k)
    l=len(plminstate)
    state=[0]*l
    for i in range(l):
        if plminstate[i]=='+':
            state[i]=1
    
    #print state
    
    counter=0
    for i in range(l-k+1):
        if state[i]==0:
            counter+=1
            for j in range(k):
                state[i+j]=1-state[i+j]
        #print state
        
    if state[l-k:l]==[1]*k:
        print "Case #{}: {}".format(tr, counter)
    else:
        print "Case #{}: IMPOSSIBLE".format(tr)

#print time.clock()-t0