from __future__ import division
import sys


def cookie(C,F,X,cost,curr):
    a=C/curr+X/(curr+F)
    b=X/curr
    if a>=b:
        return cost+X/curr
    else:
        return cookie(C,F,X,cost+(C/curr),curr+F)
    

def cookie1(C,F,X,cost,curr):
    a=C/curr+X/(curr+F)
    b=X/curr
    while(a<b):
        cost=cost+(C/curr)
        curr=curr+F
        a=C/curr+X/(curr+F)
        b=X/curr
    else:
        return cost+X/curr
        print "im done"

if __name__=="__main__":
    
    #sys.setrecursionlimit(1500)
    fo=open("B-small-attempt2.in" ,"r")
    #fo=open("input.txt" ,"r")
    number=fo.readline()
    myfile=open("2.txt","w")
    for i in range(int(number)):
        string= fo.readline()
        C,F,X=map(float,string.split())
        myfile.write("Case #"+str(i+1)+": "+str(cookie1(C,F,X,0,2.0))+"\n")
        
    myfile.close() 
        
