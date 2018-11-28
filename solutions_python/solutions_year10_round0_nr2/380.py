#optimum.py
#Run on Python 2.6.5

from fractions import gcd 

fileName = raw_input("Enter the input filename:")
f_in = open(fileName,'r')
f_out = open('OUT-'+fileName,'w')

C = int(f_in.readline())

for c in range(C):
    
    Nt = f_in.readline().split(' ')
    N, ts = Nt[0], Nt[1:]
    
    #Convert strings to long integers 
    N = int(N)    
    for i in range(N):
        ts[i] = int(ts[i])
    
    diff = [] #the absolute differences between all pairs of numbers 
    
    for i in range(N):
        for j in range(i+1,N):
            if ts[i] != ts[j]:
                diff.append(abs(ts[i] - ts[j]))
    
   
    #Find the greatest common denominators of all numbers in diff, which is T
    T = min(diff)
    
    for d in diff:
        T = gcd(T, d)
    
    #Calculate y
    if T == 1:
        y = 0
    elif min(ts) % T ==0:
        y = 0
    else:
        y = T- min(ts) % T
        
     
    f_out.write("Case #{0}: ".format(c+1)+str(y)+'\n')


print "Solved"   
f_in.close()
f_out.close()