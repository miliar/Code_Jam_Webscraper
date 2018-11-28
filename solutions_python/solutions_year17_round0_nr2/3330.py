t = int(raw_input())  # read a line with a single integer


def check_tidy(n):
    last = n % 10
    while n > 0:
        n /= 10
        if last < n % 10:
            return False
        last = n % 10
    return True


for i in xrange(1, t + 1):
    n = long(raw_input())
    if check_tidy(n):
        print "Case #{}: {}".format(i, n)
        continue

    pow10 = 1L
    while n > 0:
        pow10 *= 10L
        n -= 10L
        n /= 10L
        if check_tidy(n):
            break

    print "Case #{}: {}".format(i, n * pow10 + (pow10 - 1))