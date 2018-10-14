f = open('A-large.in')
line = f.readline().strip()

cases = int(line)

for i in range (cases):
    x = f.readline().strip()
    y = x.split()
    #y[0] = smax, y[1] = # of ppl with shylevel k
    clapping=0
    ans=0
    ppl=y[1]
    for j in range (int(y[0])+1):
        if (clapping < j):
            ans+=1
            clapping+=1
        clapping+=int(ppl[j])
    
    print("Case #{}: {}".format(i+1,ans))
    
f.close()