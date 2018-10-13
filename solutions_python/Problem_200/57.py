import sys

def split_digits(n):
    return [int(x) for x in str(n)][::-1]

def is_tidy(n):
    digits = split_digits(n)
    return list(sorted(digits, reverse=True)) == digits

def solve(n):
    while not is_tidy(n):
        digits = split_digits(n)

        to_subtract = None
        for i, digit in enumerate(digits):
            if digit != 9:
                to_subtract = 10**i
                break

        # print(f"n = {n}; to_subtract = {to_subtract}")
        assert to_subtract is not None

        n -= to_subtract

    return n

        # for i in range(len(digits)):
        #     if dik



        # split_n = split_digits(n)

        # to_subtract = None
        # for i in range(len(split_n) - 1):
        #     if [x for x in split_n[i + 1:] if x > split_n[i]]:
        #     # if split_n[i] < split_n[i + 1]:
        #         to_subtract = (split_n[i] + 1) * 10**i
        #         break

        # # print(f"n = {n}; to_subtract = {to_subtract}")

        # if to_subtract is None:
        #     return n

        # n -= to_subtract

def main():
    case_count = int(next(sys.stdin))
    for case_number in range(1, case_count + 1):
        n = int(next(sys.stdin))
        solution = solve(n)
        print(f"Case #{case_number}: {solution}")

if __name__ == "__main__":
    main()
