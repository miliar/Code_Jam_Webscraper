#!/usr/bin/python3

n = int(input())

for i in range(n):
    a = list(input())

    for j in range(len(a)-2, -1, -1):
        if a[j] > a[j+1]:
            for k in range(j+1, len(a)):
                a[k] = '9'
            a[j] = str(int(a[j]) - 1);

    print("Case #{}: {}".format(i+1, int("".join(a))))
