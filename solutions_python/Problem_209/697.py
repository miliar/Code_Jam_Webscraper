
from math import pi

nb_cases = int(input())

for caseno in range(1, nb_cases+1):
    n, k = map(int, input().split())
    dim = [tuple(map(int, input().split())) for _ in range(n)]
    dim.sort(key=lambda e: -e[0])
    R, H = zip(*dim)

    # n x (k+1) dp table
    # optimal_sa[i][j] = optimal surface area of a stack containing
    # j pancakes and having ith pancake at its base 
    optimal_sa = [[0 for i in range(k+1)] for j in range(n)]

    for i in range(n):
        optimal_sa[i][1] = (2*pi*R[i]*H[i]) + (pi*R[i]**2)

    for i in range(2, k+1):
        for j in range(n-i+1):
            optimal_sa[j][i] = max(2*pi*R[j]*H[j] + pi*(R[j]**2 - R[k]**2) + optimal_sa[k][i-1] for k in range(j+1, n))

    print('Case #{}: {}'.format(caseno, max(optimal_sa[i][k] for i in range(n))))
