f1 = open("B-small-attempt0.in","r")
f2 = open("output.txt","w")
t = f1.readline()
for l in range(int(t)):
    a,b,k = map(int,f1.readline().split())
    c = 0
    for i in range(a):
        for j in range(b):
            if i&j < k:
                c += 1
    f2.write("Case #%d: " %(l+1))
    f2.write("%d\n" %c)
        
        
        
