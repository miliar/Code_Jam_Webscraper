def solve(n, l):
    if l == 1:
        return n

    temp = ""
    while l > 1:

        end = n % 10
        n //= 10

        for i in str(n):
            if int(i) > end:
                end = 9
                temp = "9"*len(temp)
                n -= 1
                break

        temp = str(end) + temp
        l = len(str(n))

    return str(n) + temp


for i in range(int(input())):
    n = int(input())
    ans = int(solve(n, len(str(n))))
    print("Case #{}: {}".format(i+1, ans))