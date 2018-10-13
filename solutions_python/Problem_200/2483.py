T = int(input())

def decrease(digits, pos):
    if digits[pos] > 0:
        digits[pos] -= 1
    else:
        digits[pos] = 9
        decrease(digits, pos-1)

def tidy_up(digits, pos, num):
    # print(digits, pos, num)
    if pos == 0 and pos < len(digits)-1:
        return tidy_up(digits, pos+1, num)
    if digits[pos] < digits[pos-1]:
        digits[pos] = 9
        if int(''.join([str(digit) for digit in digits])) > num:
            decrease(digits, pos-1)
            tidy_up(digits, pos-1, num)
    if pos < len(digits)-1:
        return tidy_up(digits, pos+1, num) 
    return digits

def solution(num_str):
    # initiate
    digits = list(int(digit) for digit in num_str)
    digits_len = len(digits)
    num = int(num_str)
    # search tidy digits
    raw_digits = tidy_up(digits, 0, num)
    # clean leading zeros
    leading_zero_flag = True
    clean_digits = []
    for j in range(digits_len):
        if leading_zero_flag and digits[j] == 0:
            continue
        if leading_zero_flag and digits[j] != 0:
            leading_zero_flag = False
            clean_digits.append(raw_digits[j])
            continue
        if not leading_zero_flag:
            clean_digits.append(raw_digits[j])
    return ''.join([str(digit) for digit in clean_digits])

for i in range(T):
    n_s = input()
    print("Case #{}: {}".format(i+1, solution(n_s)))