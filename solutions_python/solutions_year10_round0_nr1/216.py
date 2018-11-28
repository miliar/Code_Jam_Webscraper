f=open('A-large.in','r')
g=open('A-large.out','w')
getline=f.readline()

t=int(getline)
print t


for case in range(t):
    getline=f.readline()
    eleline=getline.split()
    n=int(eleline[0])
    k=int(eleline[1])
    ans="OFF"
    if k%pow(2,n)==pow(2,n)-1:
        ans="ON"
    g.write('Case #'+str(case+1)+': '+ans+'\n')

f.close()
g.close()

            


