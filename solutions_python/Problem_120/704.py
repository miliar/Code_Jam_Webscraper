def solve(r,t):
    c=0
    while (t>= 2*r+1):
        t -= 2*r+1
        r += 2
        c += 1
    return str(c)

fi = open("A-small-attempt0.in","r")
fo = open("A-small-attempt0.out","w")

t = int(fi.readline())

for i in range(1,t+1):
    fl=fi.readline()
    d=fl.split()
    r=int(d[0])
    t=int(d[1])
    o= "Case #"+str(i)+": "+solve(r,t)
    fo.write(o+"\n")

fo.close()
fi.close()
print "Done!"
