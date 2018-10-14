# taking the number of inputs
T = int(input())

for t in range(1, T + 1):
    num = int(input())
    # converting n to list
    n = []
    while num != 0:
        r = num % 10
        num //= 10
        n = [r] + n
    lennlist = len(n)

    k = len(n)
    for i in range(len(n) - 2, -1, -1):
        if n[i] > n[i + 1]:
            n[i] -= 1
            k = i
    n = n[:k + 1] + [9 for i in range(k + 1, len(n))]
    # converting the list of numbers to number
    ans = 0
    po = len(n) - 1
    for i in range(0, len(n)):
        ans += n[i] * (10 ** po)
        po -= 1
    print("Case #{}: {}".format(t, ans))
