
# Alien Language

L, nD, N = map(int, raw_input().split())
D = []
for i in range(nD):
    D.append(raw_input())

for testcase in range(N):
    print "Case #%d:" % (testcase+1),
    P = []
    pattern = raw_input()
    a = 0
    for i in range(L):
        if pattern[a] == "(":
            b = pattern.find(")", a)
            P.append(pattern[a+1:b])
            a = b+1
        else:
            P.append(pattern[a])
            a += 1
    count = 0
    for word in D:
        good = 1
        for i in range(L):
            if word[i] not in P[i]:
                good = 0
                break
        count += good
    print count
