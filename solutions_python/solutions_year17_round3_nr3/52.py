import sys

def solve(data, amount):
    data.sort()
    data.reverse()
    total = sum(data) + amount
    count = len(data)
    average = total / count
    ans = 1
    for i in data:
        if i > average:
            total -= i
            count -= 1
            average = total / count
            ans *= i
        else: ans *= average
    return ans

def read():
    n, k = map(int, input().split())
    x = float(input())
    y = list(map(float, input().split()))
    return (y, x)

for i in range(1, int(input())+1):
    print("Case #", i, ": ", solve(*read()), sep='')
