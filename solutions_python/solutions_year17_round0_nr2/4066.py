def get_digits(n):
    digits = []
    while n:
        digits.append(n % 10)
        n /= 10
    return digits

        
def previous_tidy(n):
    digits = get_digits(n)
    previous = digits[0]
    tidy = 0
    nine_index = -1
    for i in range(len(digits)):
        if previous < digits[i]:
            digits[i] -= 1
            digits[i - 1] = 9
            nine_index = i - 1
        previous = digits[i]
    for i in range(nine_index):
        digits[i] = 9
    for i in range(len(digits)):
        tidy += digits[i] * 10 ** i
    return tidy


t = input()
for i in range(t):
    n = input()
    tidy = previous_tidy(n)
    print("Case #%s: %s" %(i + 1, tidy))

