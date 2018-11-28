def istidy(s):
    prev=0
    for i in s:
        if int(i) < prev:
            return False
        prev = int(i)
    return True

def maketidy(s):
    prev=-1
    for i, num in enumerate(s):
        if int(num) > prev:
            greater = i
        if int(num) < prev:
            s[greater] = str(int(s[greater]) - 1)
            for x in range(greater+1, len(s)):
                s[x] = '9'
            return s
        prev = int(num)
    print "ERROR"

import sys
if __name__ == "__main__":
    tests = open(sys.argv[1]).readlines()[1:]
    count = 1
    for t in tests:
        k = list(t.strip())
        if (istidy(k)):
            n = k
        else:
            n = maketidy(k)

        s = ''.join(n).lstrip('0')

        print "Case #%d: %s" % (count, s)
        count += 1

