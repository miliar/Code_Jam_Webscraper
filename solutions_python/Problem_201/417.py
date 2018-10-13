from collections import defaultdict

def get_ans(n):
    return (n - (n + 1) // 2, (n + 1) // 2 - 1)

def get_split(n):
    return (n // 2, n - n // 2 - 1)

def solve():
    n, k = map(int, input().split())
    cur = defaultdict(int)
    cur[n] += 1
    while True:
        x = max(cur)
        cnt = cur[x]
        if k <= cnt:
            return get_ans(x)
        k -= cnt
        cur.pop(x)
        for part in get_split(x):
            cur[part] += cnt

def main():
    tests = int(input())
    for test in range(1, tests + 1):
        print('Case #{}: {} {}'.format(test, *solve()))

if __name__ == '__main__':
    main()

