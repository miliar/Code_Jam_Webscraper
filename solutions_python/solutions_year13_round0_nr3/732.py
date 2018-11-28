#!/usr/bin/python3

def palindrome(n):
    return str(n) == str(n)[::-1]

fas = set()

for n in range(1, int(1e7)+1):
    if palindrome(n) and palindrome(n**2):
        fas.add(n**2)

T = int(input())
for t in range(T):
    A, B = list(map(int, input().split()))
    print("Case #{}: {}".format(t + 1, sum(map(lambda n: A <= n <= B, fas))))

