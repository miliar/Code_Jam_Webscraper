import math
import time
start_time = time.time()

f=open("B-large-1.in.txt",'r')
ntests = int(f.readline())

g = open("output.txt",'w')

def could(N,P):
    #largest power of 2<=P
    if P==0:
        return -1
    else:
        k = 0
        while 2**k<=P:
            k+=1
        k-=1
        return (2**N - 2**(N-k))
    

for i in range(ntests):
    p = f.readline()
    p = p.split()

    N = int(p[0])
    P = int(p[1])

    
    s = 2**N - could(N,2**N-P) -2
    t = could(N,P)
    
        
    g.write("Case #{}: {} {}\n".format(i+1,s,t))

    if i%1000==0:
        print(i)



    
f.close()
g.close()

print (time.time() - start_time, "secs")
