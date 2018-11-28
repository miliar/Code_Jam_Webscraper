import sys

S = 'welcome to code jam'

def completions(needle, haystack):
    total = 0
    if not needle:
        return 1
    c = needle[0]
    i = haystack.find(c)
    if i < 0:
        return 0
    return (completions(needle, haystack[i+1:]) +
            completions(needle[1:], haystack[i+1:]))


def test_case(handle):
    return completions(S, handle.next().strip())


def run(handle):
    n = int(handle.next().strip())
    for i in xrange(n):
        print 'Case #%d: %04d' % (i+1, test_case(handle) % 10000)


if __name__ == '__main__':
    run(sys.stdin)
