import math

def isPalin(num):
    rev = 0
    ori = num
    while num>0:
        c = num%10
        rev = 10*rev + c
        num /= 10
    if rev == ori:
        return True
    else:
        return False


if __name__ == "__main__":
    for case in range(input()):
        [lo, hi] = [f(i) for f, i in zip((int, int), raw_input().split())]
        lo = int(math.ceil(math.sqrt(lo)))
        hi = int(math.sqrt(hi))
        count = 0
        for n, sq in ((i, i**2) for i in xrange(lo, hi+1)):
            if isPalin(n) and isPalin(sq):
                count += 1
        print "Case #{0}: {1}".format(case+1, count)
