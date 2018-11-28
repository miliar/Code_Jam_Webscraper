x=open('C:\\Users\\Anchit\\Desktop\\A-small-attempt1.in','r')
out=open('C:\\Users\\Anchit\\Desktop\\output_file.txt','w')
a=[]
for line in x:
    a.append(line.strip())
t=int(a[0])
x1=[]
x2=[]
for i in range(1,t+1):
    c,d=map(str,a[i].split())
    x1.append(c)
    x2.append(d)
    

for i in range(t):
    x1[i]=int(x1[i][0])
    d={}
    for j in  range(x1[i]+1):
        d[j]=x2[i][j]
    
    c=0
    y=0
    
    for k in range(x1[i]+1):
        if int(d[k])!=0:
            if k<=c:    
                c=c+int(d[k])
            else:
                y=y+(k-c)
                c=c+y+int(d[k])
    s= 'Case #'+str(i+1)+': '+str(y)+'\n'    
    out.write(s)
x.close()
out.close()