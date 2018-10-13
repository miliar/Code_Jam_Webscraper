from collections import *
from heapq import *
import math
file = open("input")

counter_i = 1
counter_end_i = file.readline()
cout=0


def makelog(N,K):
    n=int(math.log(K,2))
    last=2**n
    miss = K-last+1
    base=int((N-last+1)/last)
    gap=N-last+1-base*last
    baseNum=last-gap
    h=[]
    cnt=Counter(h)
    cnt.update({base:baseNum})
    cnt.update({base+1:gap})
    cnt += Counter()
    return cnt, miss




def solve(N,K):
    cout = 0
    if 3*K>2*N+1:
	return 0,0
    cnt, newk = makelog(N,K)
    for x in range(0,newk):
        num=max(cnt)
	cnt.subtract({num: 1})
   	cnt += Counter()
    	if num%2==0:
        	if num!=0:
                	a=num/2-1
                	b=num/2
        	else:
                	return 0,0
   	else:
		if num!=1:
        		a = b = (num-1)/2
		else:
			return 0,0
    	cnt.update({b: 1})
    	cnt.update({a: 1})
    return a,b
    


while (counter_i <= int(counter_end_i.strip())):
    current_line = file.readline().strip().split(' ')
    N = int(current_line[0])
    K = int(current_line[1])
    a,b=solve(N,K)
    print "%s%d%s%d%s%d"%("Case #", counter_i,": ",b," ",a)
    counter_i=counter_i+1
