def check(s):
    curr=-1
    for i in range(len(s)):
        if int(s[i])<curr:
            return i
        curr=int(s[i])
    return -1

f_name='tst_input'
f_name='B-large.in'
rows=open(f_name,'r').readlines()
n=int(rows[0])
for tt in range(1,n+1):
    s=rows[tt].strip()
    while not check(s)==-1:
        pos=check(s)
        k=1
        ss=s
        ss=ss[:(pos-k)]+str((int(ss[pos-k])-1 ) %10) + '9'*(len(ss)-(pos-k)-1)
        k=2
        while ss[pos-k]=='0' and pos-k>0:
            ss=ss[:(pos-k)]+str((int(ss[pos-k])-1 ) %10) + '9'*(len(ss)-(pos-k)-1) 
            k=k+1
        s=ss
    if s[0]=='0':
        s=s[1:]
    print('Case #%d: %s'%(tt,s))


