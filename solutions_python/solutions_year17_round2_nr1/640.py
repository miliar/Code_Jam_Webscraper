import sys
sys.stdout = open("out.txt", "w")


def solve(d, k, s):
    pt = zip(k, s)
    pt.sort(key=lambda x: x[0],reverse=True)
    time = 0
    for p in pt:
        x = float(float(d-p[0])/p[1])
        if x>time:
            time = x
    ans = d/time

    return ans


lines = []

with open("A-large.in", "r") as f:
    lines = f.readlines()

t = int(lines[0])
ctr = 1
for i in range(1, t+1):
    fl = lines[ctr].split()
    d, n = int(fl[0]), int(fl[1])
    ctr+=1
    k ,s = [], []
    for j in range(1, n + 1):
        fl = lines[ctr].split()
        ctr+=1
        k.append(int(fl[0]))
        s.append(int(fl[1]))

    ans = solve(d, k, s)
    print("Case #{}: {}".format(i, str(ans)))
