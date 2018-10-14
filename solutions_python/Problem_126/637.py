def solve(s,n):
    c=0
    l=len(s)
    for i in range (l+1):
        for j in range (l-i+1):
            a=s[j:j+i]
            m=0
            b=0
            for k in range (len(a)):
                if (a[k] in v):
                    b=0
                else:
                    b+=1
                if (b>m):
                    m=b
            if (m>=n):
                c+=1
    return str(c)

fi = open("A-small-attempt0.in","r")
fo = open("A-small-attempt0.out","w")

v = ["a","e","i","o","u"]
                                                                 
t = int(fi.readline())

for i in range(1,t+1):
    fl=fi.readline()
    d=fl.split()
    s=d[0]
    n=int(d[1])
    o= "Case #"+str(i)+": "+solve(s,n)
    fo.write(o+"\n")

fo.close()
fi.close()
print "Done!"
