#/usr/bin/env python

def get_max_speed(H, D):
    max_speed = 9999999999999.0
    for d, s in H:
        max_speed = min(max_speed, (float(D) / (D - d)) * s)
    return max_speed

if __name__ == '__main__':
    T = int(raw_input())
    for tc in range(1, T + 1):
        D, N = map(int, raw_input().split())
        H = []
        for _ in range(N):
            H.append(map(int, raw_input().split()))
        print 'Case #%d: %.6f' %(tc, get_max_speed(H, D))
