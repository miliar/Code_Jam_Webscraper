__author__ = 'yushchenko'

t = int(input())
for i in range(t):
    n, s = input().split()
    n = int(n)
    sum = 0
    count = 0

    for j in range(n + 1):
        if (count < j):
            sum += j - count
            count = j
        count += int(s[j])

    print("Case #" + str(i + 1) + ": " + str(sum))