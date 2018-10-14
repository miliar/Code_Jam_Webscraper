import sys


def t_case():
    inp = input().split()
    s, k = list(inp[0]), int(inp[1])
    n = len(s)
    ans = 0
    for i in range(n - k + 1):
        if s[i] == '+':
            continue
        ans += 1
        for j in range(i, i + k):
            s[j] = '+' if s[j] == '-' else '-'

    if '-' in s:
        print('IMPOSSIBLE')
    else:
        print(ans)


def main():
    with open('a.in', 'r') as fin:
        with open('a.out', 'w') as fout:
            sys.stdout = fout
            sys.stdin = fin
            n = int(input())
            for i in range(n):
                print(f'Case #{i+1}: ', end='')
                t_case()


if __name__ == '__main__':
    main()
