import math,sys
fin = open('A-large.in','r')
sys.stdout = open('A-large.out','w')
    
T = int(fin.readline())
for t in range(1,T+1):
    N,M = [int(x) for x in fin.readline().split(' ')]
    s = set()
    for n in range(0,N):
        in1 = fin.readline()[:-1]
        for i in range(1,len(in1)):
            if in1[i]=='/' : s.add(in1[0:i])
        s.add(in1)
    count = 0
    for m in range(0,M):
        in1 = fin.readline()[:-1]
        for i in range(1,len(in1)):
            if in1[i]=='/' :
                if not (in1[:i] in s):
                    s.add(in1[:i])
                    count+=1
        if not (in1 in s):
                    s.add(in1)
                    count+=1             
    print('Case #%d: %d' % (t,count))
