def closest_tidy_to(number):
    digits = digits_for(number) 
    
    while not is_tidy(digits):
        index = last_index_out_of_order(digits)
        digits[index - 1] -= 1
        for i in range(index, len(digits)):
            digits[i] = 9

    return to_number(digits)

def last_index_out_of_order(digits):
    for i in range(1, len(digits) + 1):
        if digits[i - 1] > digits[i]:
            return i

def is_tidy(digits):
    return digits == sorted(digits)

def digits_for(number):
    return [int(x) for x in list(str(number))]

def to_number(digits):
    return int(''.join(str(x) for x in digits))

T = int(input())
for t in range(1, T + 1):
    number = int(input())
    result = closest_tidy_to(number)
    print('Case #{}: {}'.format(t, result))