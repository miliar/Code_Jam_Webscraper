ip=open('input.txt','r')
op=open('output.txt','w')
for i in range(int(ip.readline())):
    d,n=map(int,ip.readline().split())
    m=0
    for j in range(n):
        a,b=map(int,ip.readline().split())
        if (d-a)/b>m:
            m=(d-a)/b
    op.write("Case #"+str(i+1)+": "+str(d/m)+'\n')
    
ip.close()
op.close()
