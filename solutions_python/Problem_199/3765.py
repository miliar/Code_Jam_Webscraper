t=int(raw_input())
s=[]
k=[]
l=[]
flip=[]
result=[]
f=open('o.txt','a')
for i in range(t):
    l=raw_input().split()
    s.append(l[0])
    k.append(int(l[1]))
for i in range(t):
    flip.append(0)
for i in range(t):
    for j in range(len(s[i])-k[i]+1):
        if(s[i][j]=='-'):
            b=''
            for h in range((k[i])):
                if(s[i][j+h]=='-'):
                    b=b+'+'
                else:
                    b=b+'-'
            s[i]=s[i][:j]+b+s[i][j+len(b):]
            flip[i]+=1
        else: continue
    if(s[i].find('-')!=-1):
        result.append("IMPOSSIBLE")
    else:
        result.append(flip[i])

for i in range(t):
    m="Case #"+str(i+1)+": "+str(result[i])
    #f.write(m)
    print >>f,m
   # print m

f.close()
