f = open("B-small.in","r")
output = open("output.txt","w")
i = 0
for line in f:
    if not i:
        T = int(line.split()[0])
        i = 1
    elif i <= T:
        line = line.split()
        N = int(line.pop(0))
        S = int(line.pop(0))
        p = int(line.pop(0))
        m = 0
        for t in line:
            t = int(t)
            if t < p:
                continue
            else:
                t = t - p
                n2 = t/2
                # n3 >= n2 so no need to consider                    
                if p - n2 == 2:
                    S -= 1
                    if S < 0:
                        continue
                    else:
                        m += 1
                elif p - n2 <= 1:
                    m += 1
                else :
                    continue
        output.write("Case #"+str(i)+": "+str(m)+"\n")
        i += 1
output.close()
f.close()                          
