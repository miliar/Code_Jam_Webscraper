from math import sqrt, floor

def answer(r,t):
    a = -2*r + 1 + sqrt(4*r*r - 4*r + 1 + 8*t)
    a = a/4
    return floor(a)

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        inp = input().split()
        r,t = int(inp[0]), int(inp[1])
        d = answer(r,t)
        while 2*r*d + d*(2*d - 1) > t:
            d -= 1
        print("Case #" + str(i+1) + ": " + str(d))
