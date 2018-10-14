inp = open("C:/Users/Mariusz/Desktop/input.txt","r")
out = open("C:/Users/Mariusz/Desktop/output.txt","w")




T = int(inp.readline()[:-1])
for i in range(1,T+1):
    w = inp.readline()[:-1].split()
    pattern = []
    max_rp = int(w[0])*[0]
    max_cp = int(w[1])*[0]
    
    lawn= []
    max_cl = int(w[1])*[100]
    max_rl=int(w[0])* [100]
    
    for j in range(int(w[0])):
        t=[]
        for k in range(int(w[1])):
            t.append(100)
        lawn.append(t)

    for j in range(int(w[0])):
        t=[]
        x = inp.readline()[:-1].split()
        for k in range(int(w[1])):
            t.append(int(x[k]))
        pattern.append(t)

    for j in range(len(pattern)):
        for k in range(len(pattern[j])):
            max_rp[j] = max(max_rp[j], pattern[j][k])

    for j in range(int(w[1])):
        for k in range(int(w[0])):
            max_cp[j] = max(max_cp[j], pattern[k][j])

    r = True
    c= True
    while r and c:
        for j in range(len(pattern)):
            if max_rp[j] < max_rl[j] :
                for k in range(len(pattern[j])):
                    lawn[j][k] = min(lawn[j][k],max_rp[j])
                max_rl[j] = max_rp[j]
            else:
                if j == len(pattern)-1:
                    r = False
                    
        for j in range(int(w[1])):
            if max_cp[j] < max_cl[j]:
                for k in range(int(w[0])):
                    lawn[k][j] = min(lawn[k][j],max_cp[j])
                max_cl[j] = max_cp[j]
            else:
                if j == int(w[1])-1:
                    c = False

    if pattern == lawn:
        out.write("Case #{0}: {1}".format(i, "YES")+'\n')
    else:
        out.write("Case #{0}: {1}".format(i, "NO")+'\n')



out.close()
inp.close()
