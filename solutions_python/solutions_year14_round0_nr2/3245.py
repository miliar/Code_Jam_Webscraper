# 2 cookies per second

a = "inp.txt"
b = "out.txt"

with open(a) as f:
    inp = f.read().splitlines()
    inp = inp[1:]
    for i in range(0,len(inp)):
        tmp = inp[i].split(" ")
        for j in range(0,3):
            tmp[j] = float(tmp[j])
        inp[i] = tmp

def buy(C,F,r,X):
    if X/r > (C/r + X/(F+r)):
        return True
    return False


tlist = []
for i in inp:
    t = 0.0
    r = 2.0     # rate per second
    C = i[0]    # cost of farm
    F = i[1]    # benefit rate of farm
    X = i[2]
    while buy(C,F,r,X):
        t += C/r
        r += F
    t += X/r
    tlist.append(t)

with open(b,"w") as f:
    counter = 1
    for t in tlist: 
       f.write("Case #"+str(counter)+": "+"{0:.7f}".format(t)+"\n")
       counter += 1

