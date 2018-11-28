import sys

data = sys.stdin.read()
data = data.split("\n")

cases = int(data[0])

for i in range(1, cases+1):
    max_shyness, counts = data[i].split()
    max_shyness = int(max_shyness)
    standing = 0
    needed = 0
    for x, new in enumerate(counts):
        if standing < x:
            needed += x - standing
            standing = x
        standing += int(new)
    print("Case #%d: %d" % (i, needed))