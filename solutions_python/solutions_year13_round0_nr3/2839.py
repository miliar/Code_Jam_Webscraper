'''
Created on Apr 13, 2013

@author: melegy
'''

import math


def isfair(word):
    return word == word[::-1]
    
#def isfair(number):
#    if len(str(number)) ==1 :
#        return True
#    stack=[]
#    for c in str(number):
#        if len(stack)>0:
#            top=stack.pop()
#            if top!=c:
#                stack.append(top)
#                stack.append(c)
#        stack.append(c)
#    if len(stack)==0 :
#        return True
#    else:
#        return False
#    
if __name__=="__main__":
    inf = open('in')
    outf = open ('out','w')
    k=inf.readline()
    for i in range (1,int(k)+1):
        c=0
        line=inf.readline().split(' ')
        start=line[0]
        end=line[1]
        for n in range (int(start),int(end)+1):
            if (isfair(str(n)))  and math.sqrt(n)-int(math.sqrt(n))==0 and isfair(str(int(math.sqrt(n)))):
                c+=1
        outf.write('Case #'+str(i)+': '+str(c)+'\n')
                
            
        
        
    