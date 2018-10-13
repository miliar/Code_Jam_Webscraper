import math

def check(n):
    return str(n) == str(n)[::-1]

t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    counter = 0

    for j in range(int(math.sqrt(b)) + 179):
        if a <= j * j <= b and check(j) and check(j * j):
            counter += 1
    print('Case #' + str(i + 1) + ': ' + str(counter))
