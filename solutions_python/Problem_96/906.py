def reducetoscore(s):
    a = s//3
    t = s-3*a
    if t==2:
        return(a+1,a+1,a)
    if t==1:
        return(a+1,a,a)
    if t==0:
        return(a,a,a)

def surprising(t,p):
    (a,b,c) = t
    if (a-b)==0:
        if (a+1)>=p and b-1>=0:
            return((a+1,b-1,c))
    else:
        return((a,b,c))
    if (a-b)==1:
        if (b+1)>=p and c-1 >= 0:
            return((a,b+1,c-1))
    else:
        return((a,b,c))

def findnumber(a):
    x = a.strip().split()
    googlers = int(x[0])
    surp = int(x[1])
    p = int(x[2])
    t = x[3:]

    i=0
    while i<len(t):
        t[i] = reducetoscore(int(t[i]))
        i+=1

    i=0
    while i<len(t):
        if surp>0:
            if max(t[i])<p:
                x = surprising(t[i],p)
                if x!=t[i]:
                    t[i] = surprising(t[i],p)
                    surp-=1
            i+=1
        else:
            break
    
    count = 0
    i=0
    while i<len(t):
        if max(t[i])>=p: count+=1
        i+=1

    return(count)

inp = open('B-large.in','r')
outp = open('output_2_large.txt','w')
x = int(inp.readline())
i=0
while i<x:
    outp.write('Case #'+str(i+1)+': '+str(findnumber(inp.readline()))+'\n')
    i+=1
inp.close()
outp.close()
