#!/usr/bin/env python3

def speed(D, hb, ha):
    sb0, vb = hb
    sa0, va = ha
    if vb == va:
        return vb
    taf = (D - sa0)/va
    teq = (sa0 - sb0)/(vb - va)
    #print("taf, teq=", taf, teq)
    if teq >= 0 and teq < taf:
        seq = sb0 + vb*teq
        srem = D - seq
        tbf = srem/va
        return (D - sb0)/(teq + tbf)
    else:
        return vb

def solve(D, horses):
    #print("new case")
    horses = sorted(horses, key=lambda h: h[0])
    #print("horses bf:", horses)
    for i in range(len(horses)-2, -1, -1):
        hb = horses[i]
        ha = horses[i+1]
        sp = speed(D, hb, ha)
        horses[i] = (horses[i][0], sp)
    k, s = horses[0]
    tf = (D - k)/s
    vf = D/tf
    #print("horses af:", horses)
    return vf

def main():
    T = int(input())
    for t in range(T):
        D, N = map(int, input().split(" "))
        horses = []
        for __ in range(N):
            k, s = map(int, input().split(" "))
            horses.append((k, s))
        res = solve(D, horses)
        print("Case #{}: {:6f}".format(t+1, res))

if __name__ == "__main__":
    main()
