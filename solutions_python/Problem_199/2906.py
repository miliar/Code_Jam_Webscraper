t=int(input())
s=''
for z in range(t):
    pancake=raw_input()
    q=str(pancake)
    raw=q.split()
    k=int(raw[1])
    v=str(raw[0])
    a=[]
    w=0
    r=0
    for i in v:
        if i=='-':
            a.append('0')
        else:
            a.append('1')
    a=''.join(a)
    b=a
    l=len(a)
    f=0
    w=0
    
    for i in range(len(a)):
        if a[i]=='0' and l-k-i>=0:
            w+=1
            a=bin(int(a,2)^int('1'*k+'0'*(l-k-i),2))[2:]
            a='0'*(len(b)-len(a))+a
    for i in range(len(a)-1,-1,-1):
        if a[i]=='0' and i-k+1>=0:
            w+=1
            a=bin(int(a,2)^int('1'*k+'0'*(l-i-1),2))[2:]
            a='0'*(len(b)-len(a))+a
    if v=='+'*len(v):
        s+='Case #'+str(z+1)+': 0\n'
    else:
        if w==0 or a!='1'*len(b):
            s+='Case #'+str(z+1)+': IMPOSSIBLE\n'
        else:
            s+='Case #'+str(z+1)+': '+str(w)+'\n'
    

print(s)
