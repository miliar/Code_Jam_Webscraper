f1 = open("B-large.in","r")
f2 = open("output.txt","w")
t = f1.readline()
for j in range(int(t)):
    c, f, x = map(float, f1.readline().split())
    i = 2.0
    m = [100000000007]
    t = [0]
    l = 0
    while True :
        temp = x/i + t[l]
        if temp > m[l]:
            break
        m.append(temp)
        t.append(c/i + t[l])
        l += 1
        i += f
        
    f2.write("Case #%d: " %(j+1))
    f2.write("%.7f" %(m.pop()))
    f2.write("\n")    
        
    
    
    