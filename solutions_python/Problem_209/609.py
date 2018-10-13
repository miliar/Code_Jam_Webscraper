fname = "A-small-attempt1"

def maxArea(N,K,R,H,RH):
    RH.sort(key = lambda x: 2*x[1] + x[0]*x[0])
    use = [RH[-1]]
    RH = RH[:-1]
    
    RH.sort(key = lambda x: x[1])
    for i in range(K-1):
        use.append(RH[-1-i])
    r = max(x[0] for x in use)
    return 3.14159265358979323846264 * (2 * sum(x[1] for x in use) + r*r)

with open(fname + ".in","r") as f:
    inp = [l.strip('\n') for l in f.readlines()]

f = open(fname + ".out","w")
j=1
for i in range(int(inp[0])):
    t = inp[j].split(' ')
    N = int(t[0])
    K = int(t[1])
    R = []
    H = []
    RH = []
    j += 1
    for k in range(N):
        t = inp[j].split(' ')
        R.append(int(t[0]))
        H.append(int(t[1]))
        RH.append((int(t[0]),int(t[0]) * int(t[1])))
        j += 1
    maxA = maxArea(N,K,R,H,RH)
    f.write("Case #" + str(i+1) + ": " + str(maxA) + "\n")

f.close()
