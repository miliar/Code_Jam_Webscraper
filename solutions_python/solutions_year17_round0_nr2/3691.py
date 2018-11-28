# *-* coding:utf-8 *-*
# Problem B. Tidy Numbers
def main_result(input):
    last = "0"
    s_input = str(input)
    for i, d in enumerate(s_input):
        if d < last:
            return main_result(int(str(s_input)[0:i-1] + str(int(last) - 1) + (len(s_input) - i) * "9"))
        last = d
    return input

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    # n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    n = int(raw_input())
    result = main_result(n)
    print "Case #{}: {}".format(i, result)



