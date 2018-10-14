'''
Created on Apr 10, 2015

@author: TigerZhao
'''
t = input()

def solve(data):
    cnt =0
    standing =data[0]
    for x in range(1,len(data)):
        cur = data[x]
        if x > standing: #not enough people
            cnt += x-standing
            standing += x-standing 
        standing +=cur
    return cnt
        
for w in range(t):
    r = raw_input().strip().split()
    maxShy = int(r[0])
    data = r[1]
    data=list(data)
    data=map(int,data)
    
    print "Case #{0}: {1}".format(w+1,solve(data))