n = int(input())

def solve():
    N, R, O, Y, G, B, V = map(int, input().split())

    assert(O == G == V == 0)

    a = [(R, 'R'), (Y, 'Y'), (B, 'B')]
    a.sort(reverse=True)

    if a[0][0] > a[1][0] + a[2][0]:
        return "IMPOSSIBLE"

    res = (a[0][1] + "_") * a[0][0]


    for i in range(a[1][0]):
        res = res.replace('_', a[1][1], 1)

    for i in range(a[0][0] - a[1][0]):
        res = res.replace('_', a[2][1], 1)
    
    for i in range(a[2][0] + a[1][0] - a[0][0]):
        res = res.replace(a[0][1] + a[1][1], a[0][1] + a[2][1] + a[1][1], 1)

    return res

for i in range(1, n+1):
    print("Case #%d:" % i, solve())

"""


0000000000
1111112222
222



"""
