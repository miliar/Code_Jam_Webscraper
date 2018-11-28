import math
import time
start_time = time.time()

f = open("A.txt",'r')
ntests = int(f.readline())

g = open("output.txt",'w')

def discardmin(l,tot):
    #get rid of min to edge
    ln = len(l)

    if ln <=1:
        return [[],tot] #only max left

    mn = l[0]
    mnn = 0

    for i in range(ln):
        if l[i]<mn:
            mn = l[i]
            mnn = i

    #find min

    #move i to edge
    moves = min(mnn,ln-mnn-1)

    del l[mnn]
    return[l,tot+moves]

for i in range(ntests):
    p = f.readline()
    p = f.readline()
    q = p.split()

    for j in range(len(q)):
        q[j]= int(q[j])


    tot = 0
    for j in range(len(q)):
        s = discardmin(q,tot)
        q = s[0]
        tot = s[1]


        
    s = tot
    g.write("Case #{}: {}\n".format(i+1,s))
    
f.close()
g.close()

print (time.time() - start_time, "secs")
