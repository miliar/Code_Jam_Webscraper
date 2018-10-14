# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
def debug(line):
    # print line
    return

def flip(s, i, k):
    for j in xrange(i, i + k):
        if (s[j] == '+'):
            s[j] = '-'
        else:
            s[j] = '+'
    return s


def find_ans(s, k):
    flip_count = 0

    for i in xrange(0, len(s) - k + 1):
        c = s[i]
        if c == '-':
            debug("{} is minus so flip".format(i))
            s = flip(s, i, k)
            debug("after flip: {}".format(s))
            flip_count += 1

    for i in xrange(len(s) - k + 1, len(s)):
        c = s[i]
        if c == '-':
            return "IMPOSSIBLE"

    return flip_count

t = int(raw_input())  # read a line with a single integer
debug("test case: " + str(t))

for i in xrange(1, t + 1):
    _s, _k = [str(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    s = list(_s)
    k = int(_k)

    ans = find_ans(s, k)
    debug("Case #{}: {} {}".format(i, s, k))
    print "Case #{}: {}".format(i, ans)
    # check out .format's specification for more formatting options