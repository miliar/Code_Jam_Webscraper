import sys,math,itertools
from collections import namedtuple

if __name__ == "__main__":
    T = input()
    for t in range(T):
        N,K = map(int, raw_input().split())
        Pancake = namedtuple("Pancake", ["t","s"])
        S = lambda R, H: Pancake(R * R, 2 * R * H)
        P = [(r,h) for r,h in [map(int, raw_input().split()) for i in range(N)]]
        M = 0
        for l in list(itertools.combinations(P, K)):
            p = [S(ll[0], ll[1]) for ll in l]
            M = max(M,(max([pp.t for pp in p])+(sum(pp.s for pp in p)))*math.pi)

        #P = [S(r,h) for r,h in [map(int, raw_input().split()) for i in range(N)]]
        #P.sort(key= lambda p: p.t+p.s,reverse=True)
        #P = P[0:K]
        #P.sort(key= lambda p: p.t,reverse=True)
        #(P[0].t + sum(p.s for p in P)) * math.pi
        print("Case #%d: %.9f" % (t+1,M))
