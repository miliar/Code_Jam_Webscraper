import sys

t = int(sys.stdin.readline())
for i in range(t):
    smax, s = [x for x in sys.stdin.readline().split()]
    smax = int(smax)
    s = [int(x) for x in s]
    standing = 0
    needed = 0
    for j in range(smax+1):
        if s[j] > 0 and j > (standing + needed):
            needed += j - (standing + needed)
        standing += s[j]
    print("Case #" + str(i+1) + ": " + str(needed))