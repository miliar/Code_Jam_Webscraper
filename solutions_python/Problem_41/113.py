T=int(raw_input())
def isdec(s):
    if len(s)==1:
        return True
    tmp=s[0]
    for i in range(1,len(s)):
        if int(tmp)<int(s[i]):
            return False
    return True
def findmin(s,is0=False):

    min=int(s[1])
    number=[0 for x in range(10)]

    for i in range(10):
        number[i]=s.count(str(i))
    for i in range(1,len(s)):
        if is0:
            if int(s[i])<=min and int(s[i])>int(s[0]) and s[i]!='0':
                min=int(s[i])
        else:
            if int(s[i])<=min and int(s[i])>int(s[0]):
                min=int(s[i])
    number[int(min)]-=1
    new=str(min)
    for i in range(10):
        new+=str(i)*number[i]  
    return new

for line in range(T):

    s=raw_input()
    number=[0 for x in range(10)]
    for i in range(10):
        number[i]=s.count(str(i))
    start=len(s)
    found=False
    while start>0:
        start-=1
        if not isdec(s[start:len(s)]):
            found=True
            break
    if found:
        if start==0:
            new=s[0:start]+findmin(s[start:len(s)],True)
        else:
            new=s[0:start]+findmin(s[start:len(s)])
    else:
        min=int(s[0])
        for i in range(len(s)):
            if int(s[i])<min and int(s[i])!=0:
                min=int(s[i])
        number[min]-=1
        new=str(min)+'0'
            
        for i in range(10):
            new+=str(i)*number[i]  
    print "Case #%d: %s"%(line+1,new)
    
        
    
    
    

