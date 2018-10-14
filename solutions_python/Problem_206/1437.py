inp = open("cruisecontrol.in", 'r')
opt = open("cruisecontrol.out", 'w')

T = None
Ds = []
Hs = []
Ks = []
Ss = []
N = 0
num = True
n = 0
for line in inp:
    if T is None:
        T = int(line)
    else:
        if num:
            l = line.split(" ")
            Ds.append(int(l[0]))
            Hs.append(int(l[1]))
            Ks.append([])
            Ss.append([])
            num = False
        else:
            l = line.split(" ")
            Ks[N].append(int(l[0]))
            Ss[N].append(int(l[1]))
            n += 1
            if n == Hs[N]:
                num = True
                N += 1
                n = 0

# for each horse on the road, we need to find how long it will take to reach the destination.
# we then find the maximum time among all these times. this is how long it will take annie.
# we divide this time by the distance D to get her speed

for x in range(T):
    times = []
    H = Hs[x]
    D = Ds[x]
    ks = Ks[x]
    ss = Ss[x]
    for h in range(H):
        d = D-ks[h]
        # time = d/s
        times.append(float(d)/ss[h])
    t = max(times)
    print times, x, ks, ss, D
    S = float(D)/t
    opt.write("Case #%d: %6f\n" % (x+1, S))

opt.close()

