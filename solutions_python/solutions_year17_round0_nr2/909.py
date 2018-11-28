def output(t, res):
    casestr = "Case #" + str(t+1) +": "
    status = str(res) if res != None else "IMPOSSIBLE"
    outputLine = casestr+status
    print outputLine



def main():
    T = int( raw_input() )

    for t in xrange(T):
        n = int(raw_input())
        fixdigits = getFixDigits(n)
        while fixdigits > 0:
            #print n, fixdigits
            n /= 10**fixdigits
            n -= 1
            n *= 10**fixdigits
            n += 10**fixdigits - 1
            fixdigits = getFixDigits(n)

        output(t, n)

def getFixDigits(n):
    return len(str(n)) - tidyDigits(n) - 1

def tidyDigits(n):
    s = str(n)
    if s[0] == '0':
        print "BAAAAAD ZERO"
        return False

    for i in xrange(len(s) - 1):
        if s[i+1] < s[i]:
            return i
    return len(s) - 1

if __name__ == "__main__":
    main()