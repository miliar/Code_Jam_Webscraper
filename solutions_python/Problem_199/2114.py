reader = open("C:\\Users\\saile\\OneDrive\\codejam2017\\input2.in", "r+")
output = open("C:\\Users\\saile\\OneDrive\\codejam2017\\output2.in", "r+")
reader = reader.read().split("\n")


def flip(q):
    h = []
    for p in q:
        if p=="-":
            h.append("+")
        else:
            h.append("-")
    return(h)

for i in range(int(reader[0])):
    t = reader[i+1].split()
    s = int(t[1])
    k = list(t[0])
    f = 0
    for j in range(len(k)-s+1):
        if k[j] == "-":
            k[j:j+s] = flip(k[j:j+s])
            f=f+1
    #print(k)
    good = ["+" for i in range(s-1)]
    #print(good, k[-s+1:])
    if good != k[-s+1:]:
        output.write("Case #"+str(i+1)+":"+" IMPOSSIBLE\n")
    else:
        output.write("Case #"+str(i+1)+": "+str(f)+"\n")
output.close()
        
    
