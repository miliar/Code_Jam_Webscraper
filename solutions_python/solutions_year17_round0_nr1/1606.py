filename = input()
f = open(filename + ".in")
o = open(filename + ".out", "w")
N = int(f.readline())

for i in range(0, N):
    S, K = f.readline().split()
    K = int(K)
    t = []
    cnt = 0
    for j in range(0, len(S)):
        if S[j] == '+':
            t.append(1)
        else:
            t.append(-1)
    for j in range(0, len(t) - K + 1):
        if t[j] == -1:
            cnt += 1
            for k in range(0, K):
                t[j + k] = t[j + k] * - 1

    if sum(t) != len(S):
        print("Case #" + str(i + 1) + ": IMPOSSIBLE")
        o.write("Case #" + str(i + 1) + ": IMPOSSIBLE\n")
#        print(t)
    else:
        print("Case #" + str(i + 1) + ": " + str(cnt))
        o.write("Case #" + str(i + 1) + ": " + str(cnt) + "\n")
f.close()
o.close()
