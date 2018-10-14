from fractions import gcd

def gcd_many(nums):
    if len(nums) == 1:
        return nums[0]
    elif len(nums) == 0:
        return 1
    else:
        if len(nums) % 2 == 0:
            return gcd_many([gcd(i, j) for i, j in zip(nums[::2], nums[1::2])])
        else:
            return gcd_many([gcd(nums[0], nums[1])] + nums[2:])

def time_to_apocalypse(times):
    times = sorted(times)
    deltas = [times[i+1] - times[i] for i in range(len(times) - 1)]
    T = gcd_many(deltas)
    due_time = times[0] % T
    if due_time == 0:
        return 0
    else:
        return T - (times[0] % T)

def parse_input_and_output(infile, outfile):
    lines = open(infile).readlines()
    R = []
    for i, line in enumerate(lines[1:]):
        try:
            t = line.split()
            times = map(int, t[1:])
            res = time_to_apocalypse(times)
            R.append("Case #%d: %s" % (i + 1, res))
        except (IndexError, ValueError):
            pass
    open(outfile, "w").write("\n".join(R))
