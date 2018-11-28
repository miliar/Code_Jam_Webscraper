import sys

def isTidy(n):
    lastNum = 9
    while n > 0:
        digit = n % 10
        if digit > lastNum:
            return False
        lastNum = digit
        n /= 10
    return True

def lastTidyNum(n):
    while n > 0:
        if isTidy(n):
            return n
        n -= 1
    return 0

if __name__ == "__main__":
    fname = sys.argv[1]
    with open(fname) as f:
        content = f.readlines()
        numTests = int(content[0])
        i = 1
        for test in content[1:]:
            #n = test.split()
            result = lastTidyNum(int(test))
            print 'Case #%d: %s' % (i, result)
            i += 1
