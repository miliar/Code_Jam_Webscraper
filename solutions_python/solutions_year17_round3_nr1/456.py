#!/usr/bin/env python3

PI = 3.1415926536

def area_circ(r):
    return PI*r**2

def area_lat_cyl(r, h):
    return h*2*PI*r

def area_cyl(r, h):
    return area_circ(r) + area_lat_cyl(r, h)

def area_tot(pks):
    return sum(area_lat_cyl(*t) for t in pks) +\
        area_circ(max([t[0] for t in pks]))

def solve(N, K, pks):
    #(R, H)
    pks2 = sorted(pks, key=lambda t: area_lat_cyl(*t), reverse=True)[:K]
    #print("a", pks, pks2)
    #print("c", [t[0] for t in pks2], [t[0] for t in pks])

    r2 = max([t[0] for t in pks2])
    r = max([t[0] for t in pks])
    #print("b", r, r2)
    if r2 == r:
        return area_tot(pks2)
    else:
        a1 = area_tot(pks2)
        #print("a1 =", a1)
        minn = 0
        for i, p in enumerate(pks2):
            if area_lat_cyl(*p) < area_lat_cyl(*pks2[minn]):
                minn = i
        maxx1 = max(pks)
        pks2[minn] = maxx1
        #print("wow:", pks2)
        a2 = area_tot(pks2)
        #print("a2 =", a2)
        return max(a1, a2)

def main():
    T = int(input())
    for t in range(T):
        N, K = map(int, input().split(" "))
        pks = []
        for __ in range(N):
            pks.append(tuple(map(int, input().split(" "))))
        a = solve(N, K, pks)
        print("Case #{}: {:.9f}".format(t+1, a))

if __name__ == "__main__":
    main()
