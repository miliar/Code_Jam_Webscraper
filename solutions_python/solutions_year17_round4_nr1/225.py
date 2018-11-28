def solve():
    n, p = map(int, input().split())
    k = [0 for i in range(p)]
    a = map(int, input().split())
    for x in a:
        k[(p - x % p) % p] += 1
    ans = 0
    last = 0
    while sum(k):
        found = False
        if not last:
            ans += 1
        for i in range(p):
            if k[i] and (last + i) % p == 0:
                k[i] -= 1
                last = 0
                found = True
                break
        if not found:
            for i in range(p):
                if k[i]:
                    k[i] -= 1
                    last = (last + i) % p
                    break
    return ans

def main():
    tests = int(input())
    for test in range(1, tests + 1):
        print('Case #{}: {}'.format(test, solve()))

if __name__ == '__main__':
    main()
