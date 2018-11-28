import sys

def tree(prices, P, i=0):
    if P == 0:
        return []
    return [prices[i], tree(prices, P - 1, 2 * i + 2), tree(prices, P - 1, 2 * i + 1)]

d = {}
def solve(P, M, prices, start=0, limit=0):
    if P == 0:
        return 0
    if (P, start, limit) in d:
        return d[(P, start, limit)]
    #print(P, M, prices)
    leftprices = prices[1]
    rightprices = prices[2]
    final = prices[0]
    a = final + solve(P - 1, M, leftprices, start, limit) + solve(P - 1, M, rightprices, start + 2 ** (P - 1), limit)
    for i in range(start, start + 2 ** P):
        if M[i] == limit:
            d[(P, start, limit)] = a
            return a
    b = solve(P - 1, M, leftprices, start, limit + 1) + solve(P - 1, M, rightprices, start + 2 ** (P - 1), limit + 1)
    d[(P, start, limit)] = min(a, b)
    return min(a, b)

def main():
    T = int(input())
    for x in range(1, T + 1):
        P = int(input())
        M = list(map(int, input().split()))
        prices = []
        for i in range(P):
            for p in map(int, input().split()):
                prices.append(p)
        prices.reverse()
        prices = tree(prices, P)
        #print(P, M, prices)
        global d
        d = {}
        print("Case #{}:".format(x), solve(P, M, prices))

if __name__ == "__main__":
    with open("B-large.in") as sys.stdin:
        main()
