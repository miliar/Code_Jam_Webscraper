fi=open("C-large.in",'r')
fo=open("C-large.out",'w')

def convert(n):
    l=[]
    while (n>0):
        l.append(n%2)
        n=n/2
    return l
        
t=int(fi.readline())
for i in range(t):
    n=int(fi.readline())
    s0=fi.readline().split()
    s=[]
    for elem in s0:
        s.append(int(elem))   

    su=[0]*len(convert(max(s)))
    for j in range(len(su)):
        for elem in s:
            conv=convert(elem)
            if j<len(conv):
                su[j]+=conv[j]
    check=True
    for elem in su:
        if (elem%2==1):
            check=False
            break
    fo.write("Case #"+str(i+1)+": ")
    if (check==True):
        fo.write(str(sum(s)-min(s)))
    else:
        fo.write("NO")
    fo.write("\n")
        
fi.close()
fo.close()
    