f1=file('input3.in')
f2=file('out.txt','w')
line=f1.readline()
nt=int(line)
print nt
for j in range(nt):
    row=f1.readline()
    c,f,x = [float(y) for y in row.split()]
    #print row
   
    mintime=x/2
    r=2.0
    t=0
    while (1):
        k=c/r
        r=r+f
        t=t+k+x/r
        if(mintime<t):
            break;
        else:
            mintime=t
            t=t-x/r

    if(j!=nt-1): 
        f2.write('Case #'+repr(int(j)+1)+': '+repr(mintime)+'\n')
    if(j==nt-1):
        f2.write('Case #'+repr(int(j)+1)+': '+repr(mintime))

f2.close()
        


