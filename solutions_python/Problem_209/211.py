from math import pi

def solve(N, K, Rs, Hs):
    m = 0
    for i in range(N):
        top = pi*Rs[i]**2
        side = 2*pi*Rs[i]*Hs[i]
        tmp = [(R*H,H, R) for (R, H) in zip(Rs, Hs)]
        tmp = sorted(tmp[:i]+tmp[i+1:], reverse=True)
        s = 0
        for j in range(K-1):
            _, r, h = tmp[j]
            s += 2*pi*(r*h)
        s += side + top
        m = max(m, s)
    return m

def main():
    T = input()

    for i in range(T):
        N, K = map(int, raw_input().split())
        Rs, Hs = [], []
        for j in range(N):
            R, H = map(int, raw_input().split())
            Rs.append(R)
            Hs.append(H)
        print 'Case #%d: %.9f' % ((i+1), solve(N, K, Rs, Hs))

main()
