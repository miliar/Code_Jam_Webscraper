# -*- coding: utf-8 -*-
"""
velite
08 04 2017

google code jam
tidy numbers
"""
        
def tidy(untidy):
    
    q=list(untidy)
#    print(q)
    a=str()
    a2=str()
    if (len(q)==2):
#        print(q)
        a=str(int(q[0]))
        return a
    
    if (len(q)==3):
#        print(q)
        if int(q[0])>int(q[1]):
            a+=str(int(q[0])-1)+'9'
            return a
        else:
            a=str(int(q[0]))+str(int(q[1]))
            return a
        
    for i in range(0,len(q)-2): #q(len)=\n
        if(int(q[i+1])<int(q[i])):
            b=int(q[i])-1
            a+=str(b)     
            a+=int(len(q)-i-2)*"9"
            
            if(not i):
                a=str(b)+(len(q)-2)*'9'
                return a
                  
            if(int(q[i-1])>b):
                if(b==0):
                    for k in range(0,len(q)-2):
                        a2+='9'
                    return a2                          
                else:
                    for k in range(0,i):
                        if(int(q[k])>b):
                            a2+=str(b)
                        else:
                            a2+=str(int(q[k]))
                    for k in range(i,len(q)-1):
                        a2+='9'
                    return a2
            return a

            break  
        a+=str(int(q[i]))        
        
    a+=str(int(q[i+1])) #adding last char if still in the function
    return a


#open files 
f = open("B-small-attempt1.in", "r")
g=open("B-small-attempt1.out","w")

#read T
T=int(f.readline())

#print(T," numbers:")
for i in range (0,T-1): #analysing the first T-1 lines of the file  
    q=list(f.readline())
    if(i<T-1):
         aw=int(tidy(q))
         g.write("Case #"+str(i+1)+': '+str(aw))
         g.write('\n')

q=list(f.readline()) #last line
if(q[len(q)-1]=='\n'):
    aw=int(tidy(q))
    g.write("Case #"+str(T)+': '+str(aw))
    g.write('\n')
else:
    q.append('tt')
    aw=int(tidy(q))
    g.write(str(aw))
    g.write('\n')                
    del q





#close files
f.close()
g.close()