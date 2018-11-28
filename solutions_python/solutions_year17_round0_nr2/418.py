
def debug(line):
    # print line
    return

def minus_one(n, position):
    debug("before minus one:{}".format(str(n)))
    current_digit = int(n[position])
    if current_digit == 0:
        minus_one(n, position-1)
        n[position] = '9'
    else:
        n[position] = str(current_digit - 1)
    debug("after minus one:{}".format(str(n)))
    return n

def find_ans(n):
    for i in xrange(1, len(n)):
        prev_digit = int(n[i-1])
        current_digit = int(n[i])
        if current_digit < prev_digit:
            # make all digit to 9 after this position, and prev digit - 1
            for j in xrange(i, len(n)):
                n[j] = '9'
            n = minus_one(n, i -1)
            return False, n

    return True, n

t = int(raw_input())  # read a line with a single integer
debug("test case: " + str(t))

for i in xrange(1, t + 1):
    _n = str(raw_input())
    n = list(_n)

    debug("Finding answer {}".format(n))

    while True:
        find, ans = find_ans(n)
        if find:
            break
        debug("retrying with {}".format(str(ans)))
        n = ans

    num_ans = int("".join(ans))
    print "Case #{}: {}".format(i, num_ans)
    # check out .format's specification for more formatting options