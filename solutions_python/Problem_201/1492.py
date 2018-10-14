from math import ceil, floor

def getMaxMin(n, k):
    if k == 1:
        if n % 2 == 1:
            return ((n - 1) // 2, (n - 1) // 2)
        else:
            return (n // 2, (n - 2) // 2)

    if n % 2 == 1:
        return getMaxMin((n - 1) // 2, k // 2)
    else:
        if k % 2 == 1:
            return getMaxMin((n - 1) // 2, k // 2)
        else:
            return getMaxMin(n // 2, k // 2)



f = open('dataset.txt')
out = open('output.txt', 'w')

cases = int(f.readline())

for i in range(cases):
    case = f.readline()
    [n, k] = case.split(' ')
    n = int(n)
    k = int(k)

    (mx, mn) = getMaxMin(n, k)
    print('Case #{}: {} {}'.format(i + 1, mx, mn), file=out)
