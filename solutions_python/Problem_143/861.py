fread=open('input','r')
files=open('output','w')
n=int(fread.readline().rstrip())
a=[]	
t=long(0)
c=[]
for t in range(n):
	a=fread.readline().rstrip().split()
        c.append(0)
        for i in range(int(a[0])):
                for j in range(int(a[1])):
                        if((i & j) < int(a[2])):
                                c[t]+=1                        
g=long(1)
for t in c:
        files.write("Case #"+str(g)+": "+str(t)+"\n")
        g+=1
fread.close()
files.close()
