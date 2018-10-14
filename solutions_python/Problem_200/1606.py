def back_to_num(digits):
    return int(''.join([str(x) for x in digits])) 

def counting_on_you(digits):
    nine_spray = False

    for i in range(len(digits)-1):
        if nine_spray:
            digits[i] = 9
        elif digits[i] > digits[i+1]:
            digits[i] -= 1
            if i != 0 and digits[i] < digits[i-1]:
                digits[0] = digits[i]
                for under_spray in range(1, i+1):
                    digits[under_spray] = 9
            nine_spray = True

    if nine_spray: 
        digits[-1] = 9
    if digits[0] == 0:
        return back_to_num(digits[1:])
    else:
        return back_to_num(digits)

T = int(input())
for t in range(1, T+1):
    num = input()
    digits = [int(x) for x in num]
    last_tidy = counting_on_you(digits)
    print('Case #', t, ': ', last_tidy, sep='') 
