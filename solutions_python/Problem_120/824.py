def cost(r, n):
    return (n+1)*(1+2*n+2*r)

def main():
    num_cases = int(input())
    for case in range(1, num_cases + 1):
        r, t = map(int, input().split())
        n = 0
        while cost(r, n) <= t:
            n += 1
        print("Case #{}: {}".format(case, n))

if __name__ == '__main__':
    main()
