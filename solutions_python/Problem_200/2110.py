t = int(input())

for case in range(t):
    a = [int(x) for x in input()]

    c = 0
    l = len(a)
    while c < l - 1:
        if a[c] > a[c+1]:
            a[c] -= 1
            for i in range(c+1, l):
                a[i] = 9
            c = 0
        else:
            c += 1

    print('Case #{}: {}'.format(case + 1, int(''.join([str(y) for y in a]))))