def main2():
    s, k = input().split()
    k = int(k)
    n = len(s)
    ans = 0
    s = [True if x == '+' else False for x in s]
    flip = [False for i in range(n + 1)]
    for i in range(n - k + 1):
        if s[i] == flip[i]:
            flip[i] ^= True
            flip[i + k] ^= True
            ans += 1
        flip[i + 1] ^= flip[i]
    for i in range(n - k + 1, n):
        if s[i] == flip[i]:
            print('IMPOSSIBLE')
            return
        flip[i + 1] ^= flip[i]
    print(ans)

def main():
    n = int(input())
    for i in range(1, n + 1):
        print('Case #{}: '.format(i), end='')
        main2()

if __name__ == "__main__":
    main()
