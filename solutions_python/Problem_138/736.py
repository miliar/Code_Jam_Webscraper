def covering(naomi, ken, n):
    it = 0
    res = 0
    for i in range(n):
        while it < n and ken[it] <= naomi[i]:
            it += 1
        if it == n:
            break
        res += 1
        it += 1
    return res

def solve():
    T = int(raw_input())
    for test in range(T):
        n = int(raw_input())
        nao = sorted(map(float, raw_input().split(' ')))
        k = sorted(map(float, raw_input().split(' ')))
        war = n - covering(nao, k, n)
        deceitful = covering(k, nao, n)
        print "Case #%d: %d %d" % (test+1, deceitful, war)

if __name__ == '__main__':
    solve()
