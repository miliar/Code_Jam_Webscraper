
def test(s, p):
    if p < 0 or p > 10: return 0
    nums = [p, p - 1, p - 1]
    for i in range(3):
        if nums[i] < 0: nums[i] = 0
    if sum(nums) <= s: return 1
    nums = [p, p - 2, p - 2]
    for i in range(3):
        if nums[i] < 0: nums[i] = 0
    if sum(nums) <= s: return -1
    return 0

infile = "B-large.in"
outfile = "out.txt"

with open(outfile, "wt") as f2:
    with open(infile) as f:
        T = int(f.readline())
        for i in range(T):
            nums = map(int, f.readline().split())
            N, S, P = nums[0:3]
            nums = nums[3:]
            S1, S2 = 0, 0
            for s in nums:
                t = test(s, P)
                if t > 0: S1 += 1
                if t < 0: S2 += 1
            S1 += min(S2, S)
            f2.write("Case #" + str(i+1) + ": " + str(S1) + "\n")

