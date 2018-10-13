import sys

cin = sys.stdin
cases = int(cin.next()) # skip line saying number of cases


def gcd(a, b):
    while b:
        a, b = b, (a % b)
    return a

def lcm(a, b):
    result = a * b / gcd(a, b)
    return result


for case in range(cases):
    N, L, H = map(int, cin.next().strip().split())

    others = map(int, cin.next().strip().split())

    check = lambda x, y: (x % y == 0) or (y % x == 0)

    for freq in range(L, H+1):
        if all([check(freq, x) for x in others]):
            print("Case #%d: %d" % (case+1, freq))
            break
    else:
        print("Case #%d: NO" % (case+1,))



