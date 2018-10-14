import sys


def is_tidy(number):
    div = 1
    pos = 10
    prev = sys.maxint
    while div <= number:
        digit = (number % pos) / div
        if digit > prev:
            return False
        prev = digit
        div *= 10
        pos *= 10
    return True


def last_tidy(n):
    while n >= 1:
        if is_tidy(n):
            return n
        n -= 1

if __name__ == '__main__':
    with open("B-small-attempt0.in", "r") as f:
        t = int(f.readline())
        for i in xrange(1, t + 1):
            n = int(f.readline().strip())
            print "Case #" + str(i)+": " + str(last_tidy(n))

