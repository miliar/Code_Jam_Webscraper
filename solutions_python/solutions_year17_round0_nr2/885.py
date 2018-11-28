#tidy

def digits_in_number(number):
    return [int(x) for x in str(number)]

def non_decreasing(digits):
    non_decreasing = True
    for d in range(0,len(digits)-1):
        if digits[d]>digits[d+1]:
            non_decreasing = False
    return non_decreasing

def number_from_digits(digits):
    sum = 0
    for d in range(0,len(digits)):
        sum += digits[d] * pow(10,len(digits)-d-1)
    return sum
    
t = int(input())
for i in range(1,t+1):
    digits = digits_in_number(input())
    digit_working_on = len(digits)-1
    while non_decreasing(digits) == False:
        digits[digit_working_on] = 9
        digit_editing = digit_working_on - 1
        while digits[digit_editing] == 0:
            digits[digit_editing] = 9
            digit_editing -= 1
        digits[digit_editing] = digits[digit_editing] - 1
        digit_working_on -= 1
    output = number_from_digits(digits)
    print("Case #{}: {}".format(i,output))