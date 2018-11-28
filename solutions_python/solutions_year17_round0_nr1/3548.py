import os
os.chdir("/Users/Bastiaan/Documents")
a = open("C1.in", "r").read().split("\n")
b = int(a[0])
del(a[-1])
del(a[0])
def change(j):
    if j == "+":
        return "-"
    else:
        return "+"
print(change("+"))
for c in range(b):
    d = list(a[c].split(" "))
    e = int(d[1])
    h = len(d[0])
    g = d[0]
    cnt = 0
    for f in range(len(g)-(e-1)):
        if g[f] == "+":
            continue
        else:
            k = g[0:f]
            for u in range(f,(f+e)):
                k = k + change(g[u])
            k = k + g[(f+e):]
            g = k
            cnt = cnt + 1
    if g != h*"+":
        print("Case #" + str(c+1) + ": " + "IMPOSSIBLE")
    else:
        print("Case #" + str(c + 1) + ": " + str(cnt))
