t = int(raw_input())

for j in xrange(1, t + 1):
    n = [int(s) for s in raw_input()]  
    for i in range(len(n)-1,0,-1):
        if n[i-1]>n[i]:
            if n[i-1]==0:
                n[i-1]=9
                n[i]=9
            else:
                n[i-1]=n[i-1]-1
                n[i]=9
        if n[i-1]==0 and n[i]==0:
            n[i-1]=9
            n[i]=9
            if n[i-2]!=0:
                n[i-2]=n[i-2]-1
            
    for i in range(0,len(n)-1):
        if n[i] > n[i+1]:
            n[i+1]=9
            
    b=int(''.join(map(str, n)))
    print "Case #{}: {} ".format(j, b) 
