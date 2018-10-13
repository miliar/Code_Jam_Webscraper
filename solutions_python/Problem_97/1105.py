import string

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
def newform(n):
    s=str(n)
    combi=[]
    combi.append(s)
    for p in range(-1,-len(s),-1):
        new_s=''
        if s[p]=='0':
            continue
        for i in range(p,p+len(s)):
            new_s=new_s+s[i]
        if new_s not in combi:
            combi.append(new_s)
    return map(int,combi)

f=open('C-small-attempt0.in','r')
o=open('output.txt','w')
case=0
for line in f:
    if case==0:
        maxlines=line
        case+=1
        continue
    s=line.split()
    A=int(s[0])
    B=int(s[1])
    biglst=[]
    total=0
    for i in range(A,B+1):
        if i in biglst:
            continue
        count=0
        for e in newform(i):
            if e>=A and e<=B:
                count+=1
                biglst.append(e)
        if count>1:
            total=total+(factorial(count)/factorial(count-2)/2)
    
    o.write('Case #'+str(case)+': '+str(total)+'\n')
    case+=1


        
f.close()
o.close()


