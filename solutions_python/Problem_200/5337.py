def is_sorted(s):
    sp = [int(s) for s in str(n)]
    for i, s in enumerate(sp):
        if i < len(sp) - 1 and sp[i] > sp[i+1]:
            return False

    return True

t = int(input())
l = None

for i in range(1, t + 1):
    N = int(input())
    l = N

    if N > 20:
        for n in range(N, 1, -1):
            if is_sorted(n):
                l = n
                break

    print('Case #{}: {}'.format(i,l))

