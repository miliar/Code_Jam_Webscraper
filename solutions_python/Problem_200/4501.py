def solve(digits):
    if len(digits) == 1:
        return digits
    digits = [digits[0]] + solve(digits[1:])
    if digits[0] > digits[1]:
        digits[0] = (digits[0] - 1) % 10
        for i in range(len(digits[1:])):
            digits[i+1] = 9
    return digits

def main():
    import functools

    t = int(input())
    for i in range(1, t + 1):
        n = int(input())
        digits = list(map(lambda x: int(x), list(str(n))))
        digits = solve(digits)
        n = int(functools.reduce(lambda x,y: x+y, map(lambda x: str(x), digits)))
        print("Case #{}: {}".format(i, n))

if __name__ == "__main__":
    main()
