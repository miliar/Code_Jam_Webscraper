def isTidyNum(num):
    digits = map(int, list(str(num)))
    last_digit = 0
    for digit in digits:
        if digit < last_digit:
            return False
        last_digit = digit
    return True

def nextTidyNum(num):
    digits = list(map(int, list(str(num))))
    last_digit = 0
    new_num = []
    idx = 0
    for i in range(len(digits)):
        if digits[i] < last_digit:
            idx = i
            break
        else:
            last_digit = digits[i]
    new_num = digits[0:idx]
    new_num += [digits[idx-1]] * (len(digits) - len(new_num))
    return int("".join(map(str, new_num)))

def nextTidyNumIdx(num):
    digits = list(map(int, list(str(num))))
    last_digit = 0
    new_num = []
    idx = 0
    for i in range(len(digits)):
        if digits[i] < last_digit:
            return (digits,i)
        else:
            last_digit = digits[i]

def lastTidyNum(num):
    (digits,idx) = nextTidyNumIdx(num)
    previous_tidy_num = digits[0:idx]
    previous_tidy_num += [9] * (len(digits) - len(previous_tidy_num))
    previous_tidy_num[idx-1] -= 1

    i = 2
    while idx-i >= 0 and previous_tidy_num[idx-i] > previous_tidy_num[idx-i+1]:
        previous_tidy_num[idx-i] -= 1
        previous_tidy_num[idx-i+1] = 9
        i += 1

    # while not isTidyNum(num):
    #     num -= 1

    # return (int("".join(map(str, previous_tidy_num))), num)
    return int("".join(map(str, previous_tidy_num)))

case_num = 1
T = int(input())
for _ in range(T):
    in_num = int(input())
    if isTidyNum(in_num):
        print("Case #" + str(case_num) + ": " + str(in_num))
    else:
        print("Case #" + str(case_num) + ":" , lastTidyNum(in_num))
    case_num += 1
