# -*- coding: latin-1 -*- 

# dynamic programming
def algo(i, cash, c):
    global g, dyn, R, k, N
    
    #print "algo(" + str(i) + ", " + str(cash) + ", " + str(c) + ")"
    
    if c >= R:
        return cash
    
    if dyn[i]["visited"]:
        rounds = int((R-c) / (c - dyn[i]["c"]))
        if rounds > 0:
            return algo(i, cash + (cash-dyn[i]["cash"])*rounds,\
                        c + (c-dyn[i]["c"])*rounds)
        else:
            j = dyn[i]["nexti"]
            return algo(j, cash + dyn[j]["cash"] - dyn[i]["cash"], c+1)
    else:
        dyn[i]["visited"] = 1
        dyn[i]["cash"] = cash
        dyn[i]["c"] = c
        x = 0
        j = i
        while 1:
            if x + g[j] > k:
                break
            x += g[j]
            j = (j + 1) % N
            if j == i:
                break
        dyn[i]["nexti"] = j
        return algo(j, cash+x, c+1)

infile = open("a.in", "r")
outfile = open("a.out", "w")

T = int(infile.readline())

for x in range(T):
    tmp = (infile.readline()).split()
    R = int(tmp[0])
    k = int(tmp[1])
    N = int(tmp[2])
    tmp = (infile.readline()).split()
    g = []
    for i in range(N):
        g.append(int(tmp[i]))
    
    dyn = [{"c":0, "cash":0, "nexti":0, "visited":0} for i in range(len(tmp))]
    outfile.write("Case #" + str(x+1) + ": " + str(algo(0,0,0)) + "\n")

outfile.close()
infile.close()
