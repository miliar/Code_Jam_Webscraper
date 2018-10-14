import sys

def line():
    return sys.stdin.readline().strip()

def ints(s):
    return [int(t) for t in s.split()]


def solve(digits):
    for i in range(len(digits) - 1):
        if digits[i] < digits[i+1]:
            for j in range(i+1):
                digits[j] = 9
            digits[i+1] -= 1

    s = ''.join(str(x) for x in reversed(digits)).lstrip('0')
    return s


def main():
    tc = int(line())
    for i in range(1,tc+1):
        digits = [int(d) for d in list(line())]
        digits.reverse()
        #print digits

        print 'Case #%s: %s' % (i, solve(digits))

main()
