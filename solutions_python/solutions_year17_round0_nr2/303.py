
def increasingUntil(ints, end):
    for i in xrange(1, end):
        if ints[i] < ints[i-1]:
            return i-1
    return end-1

def calculate(ints):
    end = len(ints)
    while True:
        until = increasingUntil(ints, end)
        if until == end-1:
            break
        ints[until] = ints[until] - 1
        for i in xrange(until+1, end):
            ints[i] = 9
        end = until+1
    return int(''.join(map(str, ints)))

cases = int(raw_input())
for i in xrange(1, cases+1):
    ints = map(int, list(raw_input()))
    result = calculate(ints)
    print 'Case #%d: %d' % (i, result)
