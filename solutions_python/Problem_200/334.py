from math import floor

def tidynumber(input):
    # print 'trace', input
    lastChar = ord('9') + 1
    notTidyIdx = -1
    for i in xrange(len(input)):
        idx = len(input) - i - 1
        char = ord(input[idx])
        if char > lastChar:
            notTidyIdx = idx
            break

        lastChar = char

    if notTidyIdx < 0:
        # tidy number
        return input

    positional = 10 ** (len(input) - notTidyIdx - 1)
    return tidynumber(str(int(input) / positional * positional - 1))

for i in xrange(int(raw_input())):
    answer = tidynumber(raw_input())
    print "Case #%d: %s" % (i+1, answer)
