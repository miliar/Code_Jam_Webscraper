f1 = open("D-large.in","r")
f2 = open("output.txt","w")
t = f1.readline()
for j in range(int(t)):
    n = f1.readline()
    n = int(n)
    ar1 = map(float,f1.readline().split())
    ar2 = map(float,f1.readline().split())
    ar1.sort(cmp=None, key=None, reverse=True)
    ar2.sort(cmp=None, key=None, reverse=True)
    a1 = [i for i in ar1]
    a2 = [i for i in ar2]
    c, c1 = 0, 0
    while True:
        if a1[0]>a2[0]:
            c1 += 1
            a1.pop(0)
            a2.pop(0)
        else:
            a1.pop()
            a2.pop(0)
        if len(a1) == 0:
            break
   
    while True:
        if ar1[0]>ar2[0]:
            c += 1
            ar1.pop(0)
            ar2.pop()
        else:
            ar1.pop(0)
            ar2.pop(0)
        if len(ar1) == 0:
            break
    f2.write("Case #%d: " %(j+1))
    f2.write("%d " %c1)
    f2.write("%d " %c)
    f2.write("\n")
        
        
        