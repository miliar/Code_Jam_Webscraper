import math

def stalls(n, k):
    empty = n - k
    spaces = k+1
    prev_perfect = int(2**(math.floor(math.log(k, 2)))-1)
    # prev_perfect = int(2**(math.ceil(math.log(k+1,2)))-1)
    # print (k, prev_perfect)
    extra = k - prev_perfect

    prev_empty = n - prev_perfect
    prev_spaces = prev_perfect + 1
    min_space_width = max(int(math.floor(float(prev_empty)/prev_spaces)), 0)

    # print('min space width is %s' % min_space_width)

    n_big_spaces = prev_empty - prev_spaces*min_space_width

    half_width = (min_space_width-1)/2.0

    # do you get a big square?
    if extra > n_big_spaces:
        # print("you get a normal space")
        return (math.ceil(half_width), math.floor(half_width))

    elif math.ceil(half_width) == math.floor(half_width):
        return (math.ceil(half_width)+1, math.floor(half_width))
    else:
        return (math.ceil(half_width), math.ceil(half_width))


    # cei = int(math.ceil(float(prev_empty)/prev_spaces))

    # print "%s, %s, %s, %s, %s" % (empty, spaces, prev_empty, prev_spaces, extra)

    # min_space_width = math.floor(prev_empty/prev_spaces)

    # return (cei,flor)

if __name__ == '__main__':

    # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
      n, k = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
      res = stalls(n, k)
      # print "{}, {}".format(int(res[0]), int(res[1]))
      print "Case #{}: {} {}".format(i, int(res[0]), int(res[1]))
      # check out .format's specification for more formatting options