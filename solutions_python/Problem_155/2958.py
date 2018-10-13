import sys

lines = sys.stdin.readlines()

n_tests = int(lines[0])

for j in range(1,len(lines)):
    line = lines[j]
    if not line.strip():
        continue
    nums = line.split(" ")
    smax = int(nums[0])
    counts = [int(x) for x in nums[1].strip()]
    invites = 0
    standing = 0
    for i in range(len(counts)):
        if counts[i] == 0:
            continue
        if standing < i:
            invites += (i - standing)
            standing = i
        standing += counts[i]
    print("Case #%d: %d" % (j, invites))
