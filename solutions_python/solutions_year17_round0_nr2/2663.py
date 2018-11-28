def get_digits(n):
    return map(int, str(n))

def is_tidy(digits):
    for i in range(len(digits)-1):
        if digits[i] > digits[i+1]:
            return False
    return True

def previous_tidy(n):
    digits = get_digits(n)
    if is_tidy(digits):
        return n
    else:
        for i in range(len(digits)-1, -1, -1):
            if not is_tidy(digits[i:]):
                for j in range(i+1, len(digits)):
                    digits[j] = 9
                digits[i] -= 1
        return int(reduce(lambda x,y: x+y, map(str, digits)))

with open('B-large.in', 'r') as fd:
    t = int(fd.readline())
    for i in range(1, t+1):
        n = int(fd.readline())
        print 'Case #%d: %d' % (i, previous_tidy(n))
