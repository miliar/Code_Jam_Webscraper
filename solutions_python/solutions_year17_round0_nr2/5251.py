def check(s):
    p=str(s)
    if(len(p)==1):
        return 1
    for i in range(len(p)-1):
        if(int(p[i])-int(p[i+1])>0):
            return 0
    return 1


#print(t)
e=open("b-small-attempt1.in","r")
t=int(e.readline()[:-1])
f=open("small-attempt1.in","w")
for i in range(t):
    s=int(e.readline()[:-1])
    while(s>0):
        if(check(s)==0):
            s-=1
            #print(s)
        else:
            f.write("Case #%d: " %(i+1)+str(s)+"\n")
            break
e.close()
f.close()
