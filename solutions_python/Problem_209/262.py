from math import pi
import sys

def area(order):
    order = sorted(order, key=lambda x: x[1], reverse=True)
    S = pi * order[0][1]**2
    for rh, r, h in order:
        S += 2*pi*rh
    return S

def replace_one(order, other):
    if not other:
        return
    Ro = max(order, key=lambda x: x[1])
    Rm = max(other, key=lambda x: x[1])
    if 2*Rm[0] + Rm[1]**2 > 2*order[-1][0] + Ro[1]**2:
        order[-1] = Rm

if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())
    for t in range(1, T+1):
        N, K = sys.stdin.readline().strip().split()
        N = int(N)
        K = int(K)

        RH = []
        for n in range(N):
            r, h = sys.stdin.readline().strip().split()
            r = int(r)
            h = int(h)
            RH.append((r*h, r, h,))

        RH.sort(key=lambda x: x[0], reverse=True)
        # print(RH)
        order = RH[:K]
        # print(order)
        other = RH[K:]
        replace_one(order, other)
        S = area(order)

        print("Case #%s: %s" % (t, S))
        # print()
