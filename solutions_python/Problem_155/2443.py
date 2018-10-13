import sys

def standing_ovation(s):
    numbers = enumerate(s)
    total_added = 0
    total_standing = 0
    for i, letter in numbers:
        if i > total_standing:
            total_added += i - total_standing
            total_standing += i - total_standing
        total_standing += int(letter)
    return total_added

i = 0
with open(sys.argv[2], 'w') as o:
    for line in open(sys.argv[1], 'r'):
        if i == 0:
            i += 1
            continue
        word = line.split()[-1]
        o.write("Case #%d: %d\n" % (i, standing_ovation(word)))
        i += 1

