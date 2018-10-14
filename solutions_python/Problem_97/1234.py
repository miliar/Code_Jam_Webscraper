limit = 10000

def get_digits(number):
    digits = list()
    while number > 0:
        digits.insert(0, number % 10)
        number /= 10
    return digits

def get_number_from_digits(digits):
    number = 0
    power = 1
    digits = reversed(digits)
    for digit in digits:
        number += digit * power
        power *= 10
    return number

def rotate_digits(digits):
    return digits[1:] + digits[:1]

def get_num_recycled_pairs(number, A, B, cache):
    if cache[number]:
        return 0
    digits = get_digits(number)
    assert number == get_number_from_digits(digits)
    n = 0
    for i in xrange(len(digits)-1):
        digits = rotate_digits(digits)
        new_number = get_number_from_digits(digits)
        if cache[new_number]:
            continue
        cache[new_number] = True
        if digits[0] == 0:
            continue
        if new_number == number:
            continue
        if new_number >= A and new_number <= B:
            n += 1
    return n*(n+1)/2

def find_answer(A, B):
    cache = [False] * limit
    num_pairs = 0
    for number in xrange(A, B+1):
        num_pairs += get_num_recycled_pairs(number, A, B, cache)
    return num_pairs

f = open('C-small-attempt0.in', 'r')
N = int(f.readline())
for i in range(N):
    A,B = [int(x) for x in f.readline().split(' ')]
    print 'Case #%d: %d' % (i+1, find_answer(A, B))
f.close()
