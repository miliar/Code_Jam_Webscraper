def solve(n):
    a = [int(x) for x in str(n)]
    while True:
        for i, (digit, next_digit) in enumerate(zip(a, a[1:])):
            if digit > next_digit:
                break
        else:
            return int(''.join(str(x) for x in a))

        a[i] -= 1
        for j in range(i+1, len(a)):
            a[j] = 9


if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        r = solve(int(input()))
        print("Case #{}: {}".format(i, r))
