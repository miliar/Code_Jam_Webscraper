# B

def cookie(X, F, C):
    R = 2                   # rate
    n = 0                   # num of factories
    Min = 0
    while True:
        T = X/(R + n*F)
        for i in range(n):
            T += C/(R + i*F)
        if Min:
            if Min > T:
                Min = T
            elif Min < T:
                break
        else:
            Min = T
        n += 1
    return Min

##inptStr = """4
##30.0 1.0 2.0
##30.0 2.0 100.0
##30.50000 3.14159 1999.19990
##500.0 4.0 2000.0"""
##
##inpt = inptStr.split("\n")

f = open("B-small-attempt0.in")
inpt = []
for line in f:
    inpt.append(line.strip())
f.close()

w = open("small.out", 'w')

for i in range(int(inpt[0])):
    tmp = inpt[i+1].split(" ")
    C = float(tmp[0])
    F = float(tmp[1])
    X = float(tmp[2])
    out = "Case #{0}: {1}".format(i + 1, round(cookie(X, F, C), 7))
    w.write(out + '\n')
w.close()

print("done!")
    
