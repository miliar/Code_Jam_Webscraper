from functools import reduce

def get_tidy(number_str):
    digits = list(map(int, number_str))
    for i in range(len(digits)-1, 0, -1):
        if digits[i-1] > digits[i]:
            digits[i-1] -= 1
            digits[i:] = [9] * len(digits[i:])
    tidy = reduce(lambda x, y: x*10 + y, digits)
    return tidy

T = int(input())
for t in range(1, T+1):
    number_str = input()
    tidy = get_tidy(number_str)
    print('Case #{0}: {1}'.format(t, tidy))
