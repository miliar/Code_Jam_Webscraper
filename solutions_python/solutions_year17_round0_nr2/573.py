def last_tidy_number(number):
    i = 1
    while not is_tidy(number):
        prev = get_digit(number, i - 1)
        curr = get_digit(number, i)
        if curr > prev:
            diff = get_digits_upto(number, i - 1) + 1
            number -= diff
        i += 1
    return number


def is_tidy(n):
    digits = str(n)
    prev = '0'
    for d in digits:
        if d < prev:
            return False
        prev = d
    return True


def get_digit(number, place):
    return int(str(number)[-place - 1])


def get_digits_upto(number, place):
    return int(str(number)[-place - 1:])


n = input()
for i in range(1, n + 1):
    num = input()
    print('Case #' + str(i) + ': ' + str(last_tidy_number(num)))
