__author__ = 'Thanabhat Koomsubha'


def solve(cc):
    S, K = input().split()
    S = int(S)
    sum = 0
    sol = 0
    for i in range(S + 1):
        if int(K[i]) == 0:
            continue
        if sum < i:
            sol += (i - sum)
            sum += (i - sum)
        sum += int(K[i])
    print('Case #%d: %d' % (cc + 1, sol))


def main():
    T = int(input())
    for i in range(T):
        solve(i)


main()