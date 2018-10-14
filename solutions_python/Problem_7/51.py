def divisible(x):
    if x < 10:
        return (x == 3 or x == 6 or x == 9 or x == 0)
    return divisible(sum(map(int, str(x))))

def check(a, b, c):
    xa, ya = a
    xb, yb = b
    xc, yc = c

    if divisible(xa+xb+xc) and divisible(ya+yb+yc):
        return 1
    return 0



def run_case():
    coords = set()
    n, A, B, C, D, x0, y0, M = map(int, input().split())
    X = x0
    Y = y0
    coords.add((x0, y0))
    for i in range(1, n):
        X = (A*X+B) % M
        Y = (C*Y+D) % M
        coords.add((X, Y))

    coords = list(coords)
    n = len(coords)

    result = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                result += check(coords[i], coords[j], coords[k])
                
    return result

def main():
    
    N = int(input())
    for i in range(N):
        r = run_case()
        print('Case #%d: %s' % (i+1, r))


main()
