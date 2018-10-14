


def int_to_based_list(integer, base):


    based_list = []
    
    if integer < 0 or base <= 1:
        return based_list

    if integer == 0:
        based_list.append(integer)
        return based_list

    div = integer
    while div > 0:
        (div, rem) = divmod(div, base)
        based_list.append(rem)

    return based_list[::-1]


def based_list_to_int(based_list, base):
    
    integer = 0
    
    for digit in based_list:
        integer = integer * base + digit
        
    return integer


def largest_tidy_number(integer):
    
    digits = int_to_based_list(integer, 10)
    length = len(digits)
    
    i = 0
    peak = 0
    peak_i = 0
    while i < length and digits[i] >= peak :
        if digits[i] > peak:
            peak_i = i
            peak = digits[i]
        i += 1

    if i < length:
        if peak == 1:
            return 10 ** (length - 1) - 1
        
        x = based_list_to_int(digits[:(peak_i+1)], 10)
        x = x * (10 ** (length - peak_i-1)) - 1
        return x
        
    return integer



t = int(input())
for i in range(1, t + 1):
    n = int(input())
    largest_tidy = largest_tidy_number(n)
    print("Case #{}: {}".format(i,largest_tidy))
