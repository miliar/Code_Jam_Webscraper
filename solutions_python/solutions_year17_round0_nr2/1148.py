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

def isok(arr,ind):
    val=arr[ind]
    for i in range(ind+1,len(arr)):
        if arr[i]>val:
            return True
        if arr[i]<val:
            return False
    return True

def arr2string(arr):
    return str(arr)

t = int(raw_input())  # read a line with a single integer
for tr in xrange(1, t + 1):
    big = raw_input()
    l=len(big)
    arr=[int(x) for x in big]
    
    #print 'arr',arr
    
    i=0
    done=False
    ans=[]
    while not done:
        if i>=l:
            done=True
        else:
            if isok(arr,i):
                ans.append(arr[i])
                i+=1
            else:
                ans.append(arr[i]-1)
                ans.extend([9]*(l-i-1))
                done=True
    
    if ans[0]==0:
            ans=ans[1:]
            
    #print 'ans', ans
    
    tidy=''.join(str(x) for x in ans)
    print "Case #{}: {}".format(tr, tidy)
            
    
#print time.clock()-t0