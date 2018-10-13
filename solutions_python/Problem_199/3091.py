

T = input()
N = 1
while T > 0:
    cakes, K = input = raw_input().strip("\r\n").split()
    K = int(K)
    cakes = list(cakes)
    def flip(s):
        global cakes
        cakes[s] = (cakes[s] == "-") and "+" or "-"
    def flipper(s):
        if cakes[s] == "-":
            for i in range(s, s + K):
                flip(i)
            return 1
        return 0
    ret = 0
    for i in range(len(cakes) - K + 1):
        ret += flipper(i)
    for s in cakes[-K:]:
        if s == "-":
            ret = "IMPOSSIBLE"
            break
    print "Case #{}: {}".format(N, ret)
    T -= 1
    N += 1
