def calc(x,k):
    return (k+1)%(1<<x)
z=0
fin=open('input','r')
fout=open('out','w')
tli=[]
for line in fin:
    if z==0:
        T=int(line)
    else:
        tli=line.split()
        x=int(tli[0])
        k=int(tli[1])
        if(calc(x,k)==0):
            st="ON"
        else:
            st="OFF"
        fout.write("Case #" + str(z) + ": " + st + '\n')
    z=z+1
