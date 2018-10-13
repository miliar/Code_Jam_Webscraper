f_name='tst_input'
f_name='A-small-attempt0.in'
f_name='A-large.in'
rows=open(f_name,'r').readlines()
t=int(rows[0])
cnt=1
for tt in range(1,t+1):
    d,n=map(int,rows[cnt].split())
    maxtime=-1
    for i in range(n):
        cnt=cnt+1
        k,s=map(int,rows[cnt].split())
        left=d-k
        time=left/float(s)
        if time>maxtime:
            maxtime=time
    cnt=cnt+1
    print('Case #%d: %.6f'%(tt,d/maxtime))
