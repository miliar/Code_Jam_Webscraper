def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def gcd_all(t):
    T = 0
    for ti in t:
        for tj in t:
            dt = ti - tj
            T = gcd(T, dt)
    return T    

def solve(N, t):
    T = abs(gcd_all(t))
    return (-t[0]) % T

def main():
    for i in range(int(input())):
        N, *t = map(int, input().split())
        print("Case #{}:".format(i + 1), solve(N, t))

if __name__ == "__main__":
    main()

