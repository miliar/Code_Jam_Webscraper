import math
def ride(fl,g):
    r = int(fl[0])
    k = int(fl[1])
    n = int(fl[2])
    run = 1
    combi = [g]
    cost = []
    x=0
    while(run):
        if(sum(g[0:x])>k or x>n):
            c = sum(g[0:x-1])
            g = g[x-1:n] + g[0:x-1]
            cost.append(c)
            if g in combi:
                run=0
                rec = combi.index(g) 
            else:
                combi.append(g)
                
            x=0
        x+=1               
    if r>rec:
        init = sum(cost[0:rec])
        midval = sum(cost[rec:])*math.floor((r-rec)/len(cost[rec:]))
        last = sum(cost[rec:rec+((r-rec)%len(cost[rec:]))])    
    else:
        init = sum(cost[0:r])
        midval = 0
        last = 0    
    return init+midval+last
    
input = open("C-large.in","r")    
output = open("C-large.out","w+")
nol = input.readline()
z = 1
for i in range(int(nol)):
    fl = input.readline().split()
    sl = input.readline().split()
    ri = ride(fl,[int(i) for i in sl])
    output.write("Case #"+str(z)+": "+str(ri)+"\n")
    z+=1