def solve(fl):
    a=int(fl)
    b=str(a)
    c=len(b)
    d=0
    f=False
    while (not f) and (d<c-1):
        if b[d]<=b[d+1]:
            d+=1
        else:
            f=True
            r=False
            while (not r) and (d>0):
                if b[d]==b[d-1]:
                    d-=1
                else:
                    r=True
    if d>=c-1:
        return b
    else:
        e=b[0:d]+str(int(b[d])-1)
        for i in range (c-d-1):
            e+="9"
        if e[0]=="0":
            e=e[1:c]
        return e
        
fi = open("B-large.in","r")
fo = open("B-large.out","w")

n = int(fi.readline())

for i in range(1,n+1):
    fl = fi.readline()
    o= "Case #"+str(i)+": "+solve(fl)
    #print o
    fo.write(o+"\n")

fo.close()
fi.close()
print "Done!"
