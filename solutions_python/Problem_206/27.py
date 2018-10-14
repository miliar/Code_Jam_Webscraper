if __name__ == '__main__':

    # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        horses = []
        d, n = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
        for j in range(n):
            k, s = [float(s) for s in raw_input().split(" ")]
            horses.append((d-k)/s)

        res = d/max(horses)
        print "Case #{}: {}".format(i, res)
        # check out .format's specification for more formatting options