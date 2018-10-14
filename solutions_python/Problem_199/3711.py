# -*- coding: utf-8 -*-
"""
velite
08 04 2017

google code jam
Oversized Pancake Flipper
"""
def pb(series): 
    smart_pancakes=[]
    check=0
    j=0
    while j < len(series):
        if(series[j]=="+"):
            smart_pancakes.append(1)
            check+=1
        elif(series[j]=="-"):
            smart_pancakes.append(0)
        else:
            return smart_pancakes,j,check
        j+=1
    return smart_pancakes,j,check
            
            
def valid(total_pancakes,happy_pancakes,tool_size):
#validity of the problem, comparisson to remainder
#    print("total pancakes: ",total_pancakes)
    if(tool_size==0):
        return 0
    
    hp=int(happy_pancakes)
    if(total_pancakes < tool_size):
        return 0
#    if(hp % tool_size):
#        if((total_pancakes) % tool_size):
#            return 0
    return 1
         
def bingo(total_pancakes,happy_pancakes):
    if(total_pancakes==happy_pancakes):
        return 1
    return 0
 
   

def noma(vector,total,tool,start=0):
    flip=0
    if((start+tool)>total):
            return 0
    for i in range (start,total):
        if (int(vector[i])==0):
            
            if ((i+tool)>total):
                return 0
            flip+=1
            for j in range (i,i+tool):
                if(int(vector[j])): 
                    vector[j]=0          
                else: 
                    vector[j]=1
    return flip
                      
#open files 
f = open("A-large.in", "r")
g=open("A-large.out","w")

#read T
T=int(f.readline())



for i in range (0,T-1): #analysing the first T-1 lines of the file  
    q=f.readline()
    temp=''.join(x for x in q if x.isdigit())
    tool=int(temp)
    
    if(tool==0):
        print(i)
        break
    (vector,total,hp)=pb(q)
    if( bingo(total,hp)):
        g.write("Case #"+str(i+1)+': '+'0') #BINGOOOOOO
        g.write('\n')
    elif( not (valid(total,hp,tool)) ):
        g.write("Case #"+str(i+1)+': '+'IMPOSSIBLE')
        g.write('\n')
    else:
        res=noma(vector, total, tool)
        if (res): 
            g.write("Case #"+str(i+1)+': '+str(res))
        else:
            g.write("Case #"+str(i+1)+': '+'IMPOSSIBLE')
        g.write('\n')
    del q   
#print(noma(vector, total, tool,0))
            

q=f.readline() #reading last line
if(q[len(q)-1]=='\n'):
    pass
else:
    q+=('t') 
    
tool=int(q[len(q)-2])
(vector,total,hp)=pb(q)
if( bingo(total,hp)):
    g.write("Case #"+str(T)+': '+'0') #BINGOOOOOO
    g.write('\n')
elif( not (valid(total,hp,tool)) ):
    g.write("Case #"+str(T)+': '+'IMPOSSIBLE')
    g.write('\n')
else:
    res=noma(vector, total, tool)
    if (res): 
        g.write("Case #"+str(T)+': '+str(res))
    else:
        g.write("Case #"+str(T)+': '+'IMPOSSIBLE')
    g.write('\n')

#close files
f.close()
g.close()