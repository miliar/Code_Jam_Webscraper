import re
infile = open("C-small-attempt0.in","r")
s=infile.readline() #T
T=re.findall(r'(\d+)', s)
for t in range(int(T[0])):
    s=infile.readline() #R k N
    p=re.findall(r'(\d+)', s)
    R=int(p[0])
    k=int(p[1])
    N=int(p[2])
    s=infile.readline() #g g
    p=re.findall(r'(\d+)', s) # p contains my groups
    q=[]
    for i in range(len(p)):
        q.append(int(p[i]))
    total=0;
    curr=0
    #print R , k, N 
    #print q
    while(R):
        rev=0
        start=curr
        while(rev+q[curr]<=k):
            rev=rev+q[curr]
            curr=curr+1
            if curr==N:
                curr=0
            if curr==start:
                break
            
        R=R-1;
        total=total+rev
    print "Case #"+str(t+1)+": "+str(total)
