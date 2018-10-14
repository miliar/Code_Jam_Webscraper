f = open("dancing.small.in", "r")

T = int(f.readline())

N = []
S = []
p = []
t = []

c = []

for i in range(0, T):
    v = f.readline().split(" ")

    N.append(int(v[0]))
    S.append(int(v[1]))
    p.append(int(v[2]))
    t.append([])

    c.append(0)

    for j in range(0, N[i]):
        t[i].append(int(v[3 + j]))

f.close()



for m in range(0, T):

    remain_sup = S[m]

    for i in range(0, N[m]):
        if (t[m][i] >= 3*p[m] - min(2, t[m][i])):
            c[m] += 1
        elif (t[m][i] >= 3*p[m] - min(4, t[m][i])):
            if (remain_sup > 0):
                c[m] += 1
                remain_sup -= 1


f = open("dancing.out", "w")

for m in range(0, T):
    f.write("Case #" + str(m + 1) + ": " + str(c[m]) + "\n")

        
f.close()



print "done"
