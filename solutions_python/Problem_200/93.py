import logging
logging.basicConfig(filename='log.txt', level=logging.DEBUG)

def compute(n):
    digits = []

    while n > 0:
        digits.append(n%10)
        n = n/10
    digits = digits[::-1]
    new_digits = digits[:]
    # print digits

    for i in xrange(1, len(digits)):
        if digits[i] < digits[i-1]:
            j = i-1
            while j > 0 and digits[j] == digits[j-1]:
                j -= 1
            new_digits[j] -= 1
            for k in xrange(j+1, len(digits)):
                new_digits[k] = 9
            break

    # print new_digits

    new_digits = new_digits[::-1]
    result = 0
    for i in xrange(len(new_digits)):
        result += new_digits[i] * 10 ** i
    return result

t = int(raw_input())
for i in xrange(1, t + 1):
    logging.info("Solving case: {}".format(i))

    n, = [int(s) for s in raw_input().split(" ")]
    # print "Case #{}: {} {}".format(i, n + m, n * m)
    print "Case #{}: {}".format(i, compute(n))
