__author__ = 'Vishal'

def check_tidy(n):
    last = 11
    while n > 0:
        x = n % 10
        if x > last:
            return False
        last = x
        n /= 10
    return True

def make_tidy(n):
    digits = []
    while n > 0:
        digits.append(n % 10)
        n /= 10
    digits = list(reversed(digits))
    last_num = 0
    for pos in xrange(len(digits)):
        if digits[pos] < last_num:
            num_to_care = digits[pos - 1]
            i = pos - 1
            while digits[i] == num_to_care:
                i -= 1
                if i == -1:
                    break
            digits[i + 1] = num_to_care - 1
            '''for i in xrange(0, pos-1):
                if digits[i] > digits[pos-1]:
                    digits[i] = digits[pos-1]'''
            for i in xrange(i + 2, len(digits)):
                digits[i] = 9
            break
        else:
            last_num = digits[pos]
    #print digits
    return reduce(lambda a, b: a*10 + b, digits)

def make_tidy_naive(n):
    while n > 0:
        if check_tidy(n):
            return n
        n -= 1

inp = map(int, open("B-large.in").read().split("\n"))
o = open("output.txt", "w")
for x in xrange(1, len(inp)):
    #if make_tidy(inp[x]) != make_tidy_naive(inp[x]):
    #    print inp[x], make_tidy(inp[x]), make_tidy_naive(inp[x])
    #   break
    o.write("Case #" + str(x) + ": " + str(make_tidy(inp[x])) + "\n")
