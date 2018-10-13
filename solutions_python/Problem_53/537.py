f=open('in1.txt')
out=open('out1.txt','w')
n=int(f.readline())
for x in range(n):
    l=f.readline().split()    
    out.write("Case #%d: "%(x+1))

    if 2**(int(l[0]))-1==int(l[1])%2**int(l[0]):
       
        out.write( 'ON\n')
    else:
        out.write( 'OFF\n')
        
f.close()
out.close()
