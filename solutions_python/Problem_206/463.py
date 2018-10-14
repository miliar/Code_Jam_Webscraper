import sys
sys.stdin = open('input/A-large.in', 'r')
sys.stdout = open('out/A-large.out', 'w')

t = int(raw_input())
for i in range(t):
    horses = []
    max = 0
    D, N = [int(s) for s in raw_input().split(" ")]
    for _ in range(N):
        Ki, Si = [int(s) for s in raw_input().split(" ")]
        horses.append((Ki, Si))
        time = 1. * (D - Ki) / Si
        if time > max:
            max = time
    speed = D / max
    print "Case #{}: {}".format(i+1, speed)
