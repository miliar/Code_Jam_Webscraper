def is_tidy(n):
    return list(str(n)) == sorted(str(n))


def solve(n):
    digits = str(n)
    if is_tidy(n):
        return n
    breakpoint = min(i for i in range(len(digits) - 1) if digits[i] > digits[i + 1])
    remainder_number = int(digits[breakpoint:])
    remainder_power = (len(digits) - breakpoint - 1)
    last = str((remainder_number//(10 ** remainder_power))*(10 ** remainder_power) - 1).zfill(remainder_power + 1)
    new_n = int(digits[:breakpoint] + str(last))
    if is_tidy(new_n):
        return new_n
    else:
        return solve(new_n)


n_cases = int(input())
for i in range(n_cases):
    print('Case #{}: {}'.format(i + 1, solve(int(input()))))
