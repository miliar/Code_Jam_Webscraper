'''
Created on Apr 27, 2013

@author: akshay
'''
fp = open("A-small-attempt0 (2).in","r")
list=fp.readlines()
list=[x.strip() for x in list]
list=[x.split() for x in list]
for i in range(len(list)):
    list[i] = [int(x) for x in list[i]]
T=list.pop(0)  

for i in range(len(list)):
    r=list[i][0]
    t=list[i][1]
    count=0
    n=0
    while count <=t:
        count += (r+2*n+1)**2 - (r+2*n)**2
#        print "count =", count
        n+=1
    print "Case #%d: %d"%(i+1,n-1)
