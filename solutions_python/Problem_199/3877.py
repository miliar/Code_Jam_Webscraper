# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    s = raw_input().split(' ') # read a list of integers, 2 in this case
    row = s[0]
    size = int(s[1])

    max_try = 10000
    for n in range(0, max_try):
        if row == '+'*len(row):
            break

        idx = row.index('-')
        if (idx + size) > len(row):
            idx -= ((idx + size) - len(row))
        for x in range(idx, idx+size):
            if row[x] == '-':
                row = row[:x] + '+' + row[x + 1:]
            elif row[x] == '+':
                row = row[:x] + '-' + row[x + 1:]

        # print row

    if n == (max_try - 1):
        print "Case #{}: {}".format(i, 'IMPOSSIBLE')
    else:
        print "Case #{}: {}".format(i, n)
    # check out .format's specification for more formatting options
