T = int(input())

for t in range(1, T + 1):
    N = int(input())

    digits = [int(d) for d in str(N)]
    digit_count = len(digits)
    last_to_nine = digit_count-1
    for i in range(digit_count - 1, 0, -1):
        if digits[i] >= digits[i - 1]:
            continue

        digits[i-1] -= 1
        for j in range(i, last_to_nine+1):
            digits[j] = 9

        last_to_nine = i

    last_tidy_number = int(''.join([str(digit) for digit in digits]))

    print(f'Case #{t}: {last_tidy_number}')
