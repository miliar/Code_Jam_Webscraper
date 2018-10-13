import math

sample_input = [line.strip() for line in open('B-small-attempt0.in')]
T = int(sample_input[0])
C = sample_input[1::]

for i in range(1, T + 1):
    N = int(C[i - 1])
    str_N = str(N)
    digits = int(math.log10(N)) + 1
    threshold = int(str(bin((1 << digits) - 2))[2:]) # ick...
    
    ans = -1
    if N <= threshold:
        ans = int('9' * (digits - 1))
    else: # same number of digits
        head_digit = int(str_N[0])
        if len(str_N) == 1:
            ans = head_digit
        else:
            digit_inc_mark = 1
            digit_swp_mark = 0
            for str_digit in str_N[1:]:
                cur_digit = int(str_digit)
                if cur_digit == head_digit:
                    digit_swp_mark += 1
                if cur_digit >= head_digit:
                    digit_inc_mark += 1
                    head_digit = cur_digit
                else:
                    break
            if digit_inc_mark == digits:
                ans = N
            else:
                res = list(str_N[0:(digit_inc_mark - 1)] + \
                      ('9' * (digits - digit_inc_mark)))
                res.insert(digit_inc_mark - (digit_swp_mark + 1), str(head_digit - 1))
                res.sort()

                alt_candidate = int(res[0] + ('9' * len(res[1:])))
                if alt_candidate < N:
                    ans = alt_candidate
                else:
                    ans = int(''.join(res))
    print("Case #%i: %i" % (i, ans))

