import sys

sys.stdin = open('A-large.in')
sys.stdout = open('A-large.out', 'w')

T = int(input())
for ti in range(1, T + 1):
    l = input().split()
    smax = l[0]
    audience = l[1]
    n = 0
    ups = 0

    for i, p in enumerate(audience):
        if ups < i:
            n += i - ups
            ups = i
        ups += int(p)

    print('Case #{}: {}'.format(ti, n))
