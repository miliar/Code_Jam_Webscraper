f=file('input.in')
f2=file('output.txt','w');
line=f.readline()
t=int(line)
matrix = [[0 for x in xrange(4)] for x in xrange(4)] 
a=[]
b=[]
for k in range(t):
    ans1=int(f.readline())
    row1=f.readline()
    row2=f.readline()
    row3=f.readline()
    row4=f.readline()
    matrix[0]=row1.split();
    matrix[1]=row2.split();
    matrix[2]=row3.split();
    matrix[3]=row4.split();
    a=matrix[ans1-1]
    ans2=int(f.readline())
    row1=f.readline()
    row2=f.readline()
    row3=f.readline()
    row4=f.readline()
    matrix[0]=row1.split();
    matrix[1]=row2.split();
    matrix[2]=row3.split();
    matrix[3]=row4.split();
    b=matrix[ans2-1]
    c=0
    ans=0
    for i in range(4):
        for j in range(4):
            if(a[i]==b[j]):
                c=c+1
                ans=a[i]
    if(c==1 and k!=99):
        f2.write('Case #'+repr(k+1)+': '+ans+'\n')
    if(c>1 and k!=99):
        f2.write('Case #'+str(k+1)+': Bad magician!\n')
    if(c==0 and k!=99):
        f2.write('Case #'+str(k+1)+': Volunteer cheated!\n')
    if(c==1 and k==99):
        f2.write('Case #'+repr(k+1)+': '+ans)
    if(c>1 and k==99):
        f2.write('Case #'+str(k+1)+': Bad magician!')
    if(c==0 and k==99):
        f2.write('Case #'+str(k+1)+': Volunteer cheated!')
    
    

f.close()
f2.close()
