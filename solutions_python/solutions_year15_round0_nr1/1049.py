"""
def min_to_guarantee_so(shyness, level, standing):
    if len(shyness) == 0:
        return 0

    friends = max(level - standing, 0)

    return friends + min_to_guarantee_so(shyness[1:], level + 1, standing + int(shyness[0]) + friends)
"""

def min_to_guarantee_so(shyness):
    level = 0
    standing = 0
    friends = 0

    for s in shyness:
        frnd = max(level - standing, 0)

        level += 1
        standing += int(s) + frnd
        friends += frnd

    return friends

filename = 'A-large'
f = open(filename + '.in', 'r')
o = open(filename + '.out', 'w')

T = int(f.readline())

for t in range(T):
    smax, shyness = f.readline().split()
    shyness = list(shyness)

    o.write('Case #%d: %d\n' % (t + 1, min_to_guarantee_so(shyness)))
