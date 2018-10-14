import time
import math
s_time=time.time()


def find_number(A,B):
    def check_p(num):
        data=str(num)
        line = len(data)/2
        if line ==0:
            return True
        return data[0:line]==data[-line:]
    count =0
    a=int(math.ceil((math.sqrt(A))))
    b=int(math.sqrt(B))
    
    for i in range(a,b+1):
        if check_p(i) and check_p(i**2):
            
            count +=1
    return count
f=open('C-small-attempt0.in','r')
q= open('result.txt','w')

f.readline()
count=1

for line in f:
    A,B=line[:-1].split(' ')
    A= int(A)
    B= int(B)
    
    s='Case #'+str(count)+': '+str(find_number(A,B))+'\n'  
    count +=1  
    q.write(s)
    print 'ok'+str(count-1)
 

f.close()
q.close()
print 'seconds:',time.time()-s_time







