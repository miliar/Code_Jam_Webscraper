def is_tidy(digits):
    for i in range(len(digits)-1):
        if digits[i] > digits[i+1]:
            return False

    return True

T = int(input())
for t in range(T):
    N = int(input())
    
    digits = str(N)
    while not is_tidy(digits):
        for i in range(len(digits)-1):
            if digits[i] > digits[i+1]:
                digits = digits[:i] + str(int(digits[i]) - 1) + ('9' * (len(digits) - (i+1)))
                break

    print('Case #%d: %d' % (t+1, int(digits)))
