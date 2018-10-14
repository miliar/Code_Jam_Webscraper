import sys


def tidy(n):
    last = None
    for d in str(n):
        if last is not None and d < last:
            return False
        last = d
    return True


def find_last_tidy(str_n):
    # str_n = str(n)
    mind = None
    flip = None
    for i in range(len(str_n) - 1, -1, -1):
        d = str_n[i]
        if mind is None:
            mind = d
        else:
            mind = min(d, mind)
        if d > mind:
            flip = i
            mind = str(int(d) - 1)
        pass

    if flip is None:
        return str_n

    prefix = str_n[:flip] if flip > 0 else ""
    flip_digit = str(int(str_n[flip]) - 1)
    if flip == 0 and str_n[0] == "1":
        flip_digit = ""
    suffix = "9" * (len(str_n) - flip - 1)

    # print [prefix, flip_digit, suffix, flip]
    return "".join([prefix, flip_digit, suffix])


# last_tidy = None
# for i in range(100001):
#     if tidy(i):
#         last_tidy = i
#     if str(last_tidy) != find_last_tidy(str(i)):
#         print i, last_tidy, tidy(i), find_last_tidy(i)
#         break
# print 'DONE!'


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    for i in range(N):
        x = sys.stdin.readline().strip()
        print "Case #%d: %s" % (i + 1, find_last_tidy(x))
