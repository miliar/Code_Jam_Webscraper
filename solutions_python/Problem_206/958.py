import sys
#sys.stdin = open('a.txt', 'r')
sys.stdout = open('answer.txt', 'w')
def solve():
    d, n = map(int, input().split())
    ans = -1
    for i in range(n):
        k, s = map(int, input().split())
        tt = (d - k) / s
        ans = max(ans, tt)
    print(d / ans)

t = int(input())
for i in range(1, t + 1):
    print('Case ', '#', i, ': ', end = '', sep = '')
    solve()
sys.stdout.close()
