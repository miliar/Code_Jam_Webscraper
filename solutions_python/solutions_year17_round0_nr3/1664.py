import math
filename = input()
f = open(filename + ".in")
o = open(filename + ".out", "w")
T = int(f.readline())

delim = [0]
lim = 0
for i in range(0, 60):
    lim += pow(2, i)
    delim.append(lim)

for i in range(0, T):
    K, N = list(map(int, f.readline().split()))
    if K == N or N > delim[int(math.log2(K))]:
        print ("Case #" + str(i + 1) + ": 0 0")
        o.write ("Case #" + str(i + 1) + ": 0 0\n")
        continue

    cur = 0
    for j in range(0, len(delim)):
        if delim[j] < N:
            cur = j
    n = N - delim[cur]

    res = []

    orig = ()
    if K % 2 == 0:
        orig = (int(K / 2), int(K / 2) - 1)
    else:
        orig = (int((K - 1) / 2), int((K - 1) / 2))
    if N == 1:
        print("Case #" + str(i + 1) + ": " + str(orig[0]) + " " + str(orig[1]))
        o.write ("Case #" + str(i + 1) + ": " + str(orig[0]) + " " + str(orig[1]) + "\n")
        continue
    mx = max(orig)
    mn = min(orig)
    if mx == mn:
        res = [mx, -1, 2, 0]
    else:
        res = [mx, mn, 1, 1]

    for j in range(0, cur -1):
        mx = res[0]
        mn = res[1]
        if mx == mn:
            mn = -1
        
        val1 = ()
        val2 = ()
        if mx % 2 == 0:
            val1 = (int(mx / 2), int(mx / 2) - 1)
        else:
            val1 = (int((mx - 1) / 2), int((mx - 1) / 2))
        if mn != -1 and mn % 2 == 0:
            val2 = (int(mn / 2), int(mn / 2) - 1)
        elif mn != -1:
            val2 = (int((mn - 1) / 2), int((mn - 1) / 2))

        new_mx = max(val1)
        new_mn = min(val1)
        if mn != -1:
            new_mn = min(new_mn, min(val2))
        new_mx_cnt = val1.count(new_mx) * res[2]
        new_mn_cnt = 0
        if new_mx != new_mn:
            new_mn_cnt = val1.count(new_mn) * res[2]
        if mn != -1:
            new_mx_cnt += val2.count(new_mx) * res[3]
            new_mn_cnt += val2.count(new_mn) * res[3]
        res[0] = new_mx
        res[1] = new_mn
        res[2] = new_mx_cnt
        res[3] = new_mn_cnt
#        print(str(res[0]) + "," + str(res[1]) + ":res[2]=" + str(res[2]) + ",res[3]=" + str(res[3]))
#    print(res[0])
#    print(res[1])
#    print("n=" + str(n) + ", res[2]=" + str(res[2]) + ",res[3]=" + str(res[3]))
    val = 0
    if n <= res[2]:
        val = res[0]
    else:
        val = res[1]
    res_large = 0
    res_small = 0
    if val % 2 == 0:
        res_large = int(val / 2)
        res_small = int(val / 2) - 1
    else:
        res_large = int((val - 1) / 2)
        res_small = int((val - 1) / 2)
    print ("Case #" + str(i + 1) + ": " + str(res_large) + " " + str(res_small))
    o.write ("Case #" + str(i + 1) + ": " + str(res_large) + " " + str(res_small) + "\n")

f.close()
o.close()
