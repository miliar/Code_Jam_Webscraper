def find_tidy(num):
    n = 0
    while n < len(str(num)) - 1:
        d = num // 10**n % 10
        e = num // 10**(n + 1) % 10

        if d == 0 or d < e:
            # num -= (d + 1) * 10 ** n
            num -= (num % 10 ** (n + 1)) + 1
        n += 1

    return str(num)


t = int(input())
for i in range(1, t + 1):
    n = int(input())
    print("Case #" + str(i) + ": " + find_tidy(n))
