import sys
import re

num_cases = int(sys.stdin.readline().strip())

def sub1(num_str, i):
    while i > 0:
        if num_str[i] == "-1":
            num_str[i] = 0
            num_str[i - 1] = str(int(num_str[i - 1]))
            i -= 1
        else:
            break
    return i


def get_tidy(num_str):
    for i in reversed(range(1, len(num_str))):
        if int(num_str[i]) < int(num_str[i - 1]):
            num_str[i] = "9"
            num_str[i - 1] = str(int(num_str[i - 1]) - 1)
            # print i, num_str
            start_pos = sub1(num_str, i - 1)
            for j in xrange(start_pos + 1, len(num_str)):
                num_str[j] = "9"

    joined = "".join(num_str)
    return re.sub("^0+", '', joined)
        

for case in xrange(num_cases):
    num_str = list(sys.stdin.readline().strip())
    tidy = get_tidy(num_str)
    print "Case #%d: %s" % (case + 1, tidy)
