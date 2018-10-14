import sys

t = int(input())
happy = '+'
blank = '-'
lines = sys.stdin.read().splitlines()
i = 0
for line in lines:
    i += 1
    n, m = line.split(' ')
    n = list(n)
    m = int(m)
    output = 0
    for t in range(0, len(n)):
        if n[t] == blank:
            if len(n) - t >= m:
                output += 1
                for s in range(t, t + m):
                    if n[s] == blank:
                        n[s] = happy
                    else:
                        n[s] = blank
            else:
                if blank in n:
                    output = 'IMPOSSIBLE'

    print("Case #{}: {}".format(i, output))


