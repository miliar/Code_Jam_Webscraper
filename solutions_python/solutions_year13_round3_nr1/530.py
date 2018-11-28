'''
Created on Apr 12, 2013

@author: Moatasem
'''
import math

def getSubStrings(s):
  substrings=[]
  for i in xrange(len(s)):
       for j in range(i+1,len(s)+1):
             substrings.append( s[i:j])
       
  return substrings


def getConsectiveConsountsCount(s,n):
    maxCons=0
    for j in range(0,len(s)):
        if(s[j]<>'a'and s[j]<>'e' and s[j]<>'i' and s[j]<>'o' and s[j]<>'u'):
            maxCons+=1
        else: 
             maxCons=0
        if(n==maxCons):
            return 1;
        
    return 0
        
def getSolution(s,n):
    sub= getSubStrings(s)
    c=0
    for i in range(len(sub)):
        c+= getConsectiveConsountsCount(sub[i],n)
    return c
    
    

f_r = open('A.in',"r")
n_test=int(f_r.readline().strip()) 
print n_test
result=""
f_w = open("A.out", "w")
for i in range(n_test):
    temp=f_r.readline().strip().split()
    res= getSolution(temp[0], int(temp[1]))
   # print temp
    output_str='Case #{itr}: {res}'.format(itr=(i+1),res=res)
    f_w.write(output_str+'\n')
f_r.close()
f_w.close()
