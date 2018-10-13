import fileinput
kase = 0
for line in fileinput.input():
    if kase == 0:
        kase += 1
        continue
    _, s = line.split()
    friendCount = 0
    standCount = 0
    for fluttershy in range(0, len(s)):
        friendCount += max(0, fluttershy - standCount)
        standCount = max(fluttershy, standCount) + int(s[fluttershy])
    print("Case #{}: {}".format(kase, friendCount))
    kase += 1
