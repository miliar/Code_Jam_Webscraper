x='inp.txt'


with open(x,'r') as Z:
    i=Z.readlines()

t=int(i[0])
i=''.join(i[1:]).split('\n')[:-1]
#print(i)
zds=[]
for s in range(t):
    n=int(i[2*s])
    x=i[2*s+1].split()
    for w in range(len(x)):
        x[w]=int(x[w])
    #print(x)
    x.sort();x.reverse()
    q=x[0]
    y=x[1:]
    for z in y:
        q^=z
    if q==0:
        o=0
        for w in x[:-1]:
            o+=w
        zds.append(o)
    else:
        zds.append('NO')
        
   
z_=open('out.txt','w')
for d in range(len(zds)):z_.write('Case #'+str(d+1)+': '+str(zds[d])+'\n')
z_.close()

print('end')

  
