rd = input

def solve(p, k):
    p, k = list(p), int(k)
    flips = 0
    try:
        i = 0
        while True:
            i = p.index('-', i)
            if i + k <= len(p):
                flips += 1
                for j in range(i, i+k):
                    p[j] = '+' if p[j] == '-' else '-'
            else:
                return 'IMPOSSIBLE'
    except ValueError:
        return flips

for t in range(1, 1+int(rd())):
    print('Case #{}: {}'.format(t, solve(*rd().split())))
