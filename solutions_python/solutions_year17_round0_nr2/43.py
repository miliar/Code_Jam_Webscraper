# Time:  O((logn)^2)
# Space: O(logn)

def tidy_numbers():
    digits = map(int, list(raw_input().strip()))
    for i in reversed(xrange(1, len(digits))):
        if digits[i] == 0 or digits[i] < digits[i-1]:
            for j in xrange(i, len(digits)):
                digits[j] = 9
            for j in reversed(xrange(i)):
                if digits[j] != 0:
                     digits[j] -= 1
                     break
                else:
                    digits[j] = 9
    return int("".join(map(str, digits)))

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, tidy_numbers())
