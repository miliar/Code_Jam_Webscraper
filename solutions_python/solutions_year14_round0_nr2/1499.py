def farmcost(n, C, F, dic={}):
    if n in dic:
        return dic[n]
    if n == 0:
        return 0
    dic[n] = farmcost(n - 1, C, F, dic) + (C / (2 + (n - 1) * F))
    return dic[n]

def totalcost(n, C, F, X, diccost={}):
    return farmcost(n, C, F, diccost) + X / (2 + n * F)

def findbestcost(C, F, X):
    dic = {}
    curn = 0
    lastbest = float("inf")
    curbest = totalcost(curn, C, F, X, dic)
    while curbest < lastbest:
        curn += 1
        lastbest = curbest
        curbest = totalcost(curn, C, F, X, dic)
    return lastbest

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        C, F, X = [float(x) for x in input().split()]
        best = findbestcost(C, F, X)
        print ("Case #{}: {:.7f}".format(t + 1, best))

