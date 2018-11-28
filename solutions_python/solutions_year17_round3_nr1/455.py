import sys,math
sys.stdout = open("out.txt", "w")


def solve(k, r, h):
    cakes = zip(r, h)
    cakes.sort(key=lambda x: x[0]*x[1],reverse=True)
    ans = 0
    for i in range(len(cakes)):
        base = cakes[i]
        cur_ans = base[0]*(base[0]+2*base[1])
        ctr = 1
        for j in range(len(cakes)):
            if i==j:
                continue
            if ctr==k:
                break
            if base[0]>=cakes[j][0]:
                cur_ans+=(cakes[j][0]*2*cakes[j][1])
                ctr+=1
        if cur_ans>ans:
            ans=cur_ans
    return ans*math.pi


lines = []

with open("A-large.in", "r") as f:
    lines = f.readlines()

t = int(lines[0])
ctr = 1
for i in range(1, t+1):
    fl = lines[ctr].split()
    n, k = int(fl[0]), int(fl[1])
    ctr+=1
    r ,h = [], []
    for j in range(1, n + 1):
        fl = lines[ctr].split()
        ctr+=1
        r.append(int(fl[0]))
        h.append(int(fl[1]))

    ans = solve(k, r, h)
    print("Case #{}: {}".format(i, str(ans)))
