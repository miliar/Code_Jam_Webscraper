# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

possibles = ['R', 'O', 'Y', 'G', 'B', 'V']

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    params = [int(s) for s in raw_input().split(" ")]
    n = params[0]
    nums = params[1:]

    small = [{"key":"R", "num":nums[0]}, {"key":"Y", "num":nums[2]}, {"key":"B", "num":nums[4]}]
    small = sorted(small, key = lambda x: x["num"], reverse = True)

    if small[0]["num"] > n/2:
        print "Case #{}: IMPOSSIBLE".format(i)
        continue

    finish = False

    ret = ""

    while not finish:
        if small[0]["num"] > small[1]["num"]:
            ret = ret + small[0]["key"] + small[1]["key"] + small[0]["key"] + small[2]["key"]
            small[0]["num"] -= 2
            small[1]["num"] -= 1
            small[2]["num"] -= 1
        else:
            ret = ret + small[0]["key"] + small[1]["key"]
            small[0]["num"] -= 1
            small[1]["num"] -= 1

            if small[2]["num"] > 0:
                ret = ret + small[2]["key"]
                small[2]["num"] -= 1
        if small[0]["num"] <= 0:
            finish = True

    print "Case #{}: {}".format(i, ret)

#    else:

    # check out .format's specification for more formatting options

