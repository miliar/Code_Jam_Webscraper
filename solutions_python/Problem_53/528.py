f=open('A-large.in','r')
fo=open('output.txt','w')
t=int(f.readline())
for i in range(t):
    n,k=f.readline().split()
    n,k=int(n),int(k)
    a=(k+1)/(2**n)
    if a.is_integer():
        fo.write('Case #{0}: ON\n'.format(i+1))
    else:
        fo.write('Case #{0}: OFF\n'.format(i+1))
