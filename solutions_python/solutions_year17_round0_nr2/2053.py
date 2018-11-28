def all_inc(ar):
    for i, item in enumerate(ar):
        if i > 0 and item < ar[i-1]:
            return False
    return True

def first_decreasing(ar):
    for i, item in enumerate(ar):
        if i > 0 and item < ar[i-1]:
            return i

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arN = [int(n) for n in str(N)]

    while (not all_inc(arN)):
        d = first_decreasing(arN)
        arN[d-1] -= 1
        for i in range(d, len(arN)):
            arN[i] = 9
        
    tidy = int(''.join([str(n) for n in arN]))
    print("Case #{}: {}".format(t, tidy))
