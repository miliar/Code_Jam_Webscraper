def main():
    num_cases = int(input())
    for case in range(1, num_cases + 1):
        c, f, x = map(float,input().split())
        r = 2.0
        t = 0.0

        while x/r > c/r + x/(r+f):
            t += c/r
            r += f

        t += x/r
        
        print("Case #{}: {}".format(case, t))

if __name__ == '__main__':
    main()
