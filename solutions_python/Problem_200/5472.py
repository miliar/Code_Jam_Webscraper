def is_tidy(target):
    s = [int(x) for x in str(target)]
    for i in range(len(s) - 1):
        if s[i] > s[i + 1]:
            return False
    return True


def get_last_tidy(n):
    target = n
    while target > 0:
        if is_tidy(target):
            return target
        target = target - 1


# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n = int(raw_input())
    print 'Case #' + str(i) + ': ' + str(get_last_tidy(n))
    # n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    # print "Case #{}: {} {}".format(i, n + m, n * m)
    # check out .format's specification for more formatting options
