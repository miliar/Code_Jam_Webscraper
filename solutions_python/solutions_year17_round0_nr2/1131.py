def solve(x):
    digits = [int(i) for i in str(x)]
    for i, digit in enumerate(digits):
        if i > 0 and digit < digits[i - 1]:
            for j in range(i, len(digits)):
                digits[j] = 9
            digits[i - 1] = digits[i - 1] - 1
            return solve(int(''.join(str(digit) for digit in digits)))
    return x


def main():
    T = int(input())
    for case in range(T):
        N = int(input())
        print("Case #{}: {}".format(case + 1, solve(N)))


if __name__ == '__main__':
    main()
