import sys

t = int(sys.stdin.readline().strip())

for case in range(1, t + 1):
    needed = 0
    standing = 0
    levels, counts = sys.stdin.readline().strip().split()
    for level in range(int(levels)+1):
        if standing < level:
            if int(counts[level]) != 0:
                needed += (level - standing)
                standing = level 
        standing += int(counts[level])
    print("Case #{}: {}".format(case, needed))

