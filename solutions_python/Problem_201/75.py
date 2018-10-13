import numpy as np
import heapq


def getparts(n):
    if(n%2==1):
        return str((n-1)/2)+" "+str((n-1)/2);
    else:
        return str((n+1)/2)+" "+str((n-1)/2);

def solve(n, k):

    k-=1;
    
    
    counts = np.array([1,0]);
    newcounts = np.array([0,0]);
    
    while(k>0):
        
#         print counts,n,k
                
        k-=counts[1];
        
        if(k>=0):
            k-=counts[0];
            
            if(k>=0):
                newn = (n-1)/2;
                if(n%2==0): ## n=24, newn=11
                    newcounts[0] = counts[0];
                    newcounts[1] = counts[0] + 2*counts[1];
                else: ## n=25, newn=12
                    newcounts[0] = counts[0]*2 + counts[1];
                    newcounts[1] = counts[1];

                counts = newcounts;
                n = newn;
            else:
                return getparts(n);
            
        else:
            return getparts(n+1);   
    
    
#     print n,k,counts        
    return getparts(n+1) if counts[1]>0 else getparts(n);
            
        
    
# f = file('/home/jabot/Downloads/2017_q3_sample.in');
# fout = file('/home/jabot/Downloads/2017_q3_sample.out','w');

f = file('/home/jabot/Downloads/C-large.in');
fout = file('/home/jabot/Downloads/C-large.out','w');

lines = f.readlines();
print lines
n = int(lines[0]);
cnt=0;
for l in lines[1:n+1]:
    cnt+=1;
    #print np.array(l.strip().split(' ')[1:],int)
    print '---'
    [n,k] = l.split(' ');
    out = solve(int(n), int(k));
    
    print out;
    
    fout.write('Case #'+str(cnt)+": "+out+"\n");
    

