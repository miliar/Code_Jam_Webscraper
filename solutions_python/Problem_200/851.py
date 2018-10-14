n = int(input())
for q in range(n):
    n = list(map(int, input().strip()))
    s = len(n)

    for i in range(s-2, -1, -1):
        if n[i] > n[i+1]:
            n[i] -= 1
            n[i+1:] = '9'*(s-i-1)

    num = ''.join(map(str, n))
    num = num.lstrip('0')

    print("Case #{}: {}".format(q+1, num))
