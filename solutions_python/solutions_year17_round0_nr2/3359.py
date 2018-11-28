#import numpy

def tidy(N):
    m = N
    digits = list(int(d) for d in str(m))
    previous = digits[0]
    i = 1
    while i < len(digits):
        if digits[i] < previous:
            for j in range(i, len(digits)):
                digits[j] = 9
            digits[i-1] -= 1
            i = 0
        previous = digits[i]
        i += 1

    return int(''.join(str(d) for d in digits))

if __name__ == '__main__':
    for T in range(int(raw_input().strip())):
        N = int(raw_input().strip())
        print "Case #%d: %d" % (T+1, tidy(N))