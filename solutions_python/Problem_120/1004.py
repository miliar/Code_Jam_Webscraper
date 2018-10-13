'''
Created on 26-Apr-2013

@author: amit
'''

from __future__ import division
import math


def getNumberOfRings(f):
    r, t=f.readline().split(' ')
    r=int(r)
    t=int(t)
    totalringsguess=1
    needed=getPaintForNRings(totalringsguess, r)
    while(t-needed>=0):
        
        totalringsguess*=2
        needed=getPaintForNRings(totalringsguess, r)
    
    high=totalringsguess
    low=totalringsguess/2
    mid=math.floor((low+high)/2)
    diff=-1
    while(low<=high):
        
        mid=math.floor((low+high)/2)
        
        needed=getPaintForNRings(mid, r)
        diff=t-needed
        if(diff>0):
            low=mid+1
        elif(diff<0):
            high=mid-1
        elif(diff==0):
            break
    
    if(diff==0):
        return mid
    
    return low-1
    
    
def getPaintForNRings(n,r):
    #return (2*r+1)*n + 4*(n*(2*n-3) + 2)
    return ((n+r)*2-1)*n

def main():
    i=1
    f=open('input.txt','r')
    fout=open('output.txt','w')
    t=int(f.readline())
    
    while(t!=0):
        
        ans=getNumberOfRings(f)
        fout.write("Case #{}: {}\n".format(i,int(ans)))
        #print "Case #{}: {}".format(i,int(ans))
        i+=1
        t-=1

    fout.close()
    f.close()
    
if __name__=="__main__":
    main()
    #print getPaintForNRings(2,1)