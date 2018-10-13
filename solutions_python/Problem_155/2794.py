#inp = open('A-small-attempt0.in', 'r')
inp = open('A-large.in', 'r')
out = open('output.txt', 'w')

size = int(inp.readline())
case = 1
for line in inp.readlines():
    line = line.split(' ')
    max_shyness = int(line[0])
    auditory = line[1]
    total = 0
    needed = 0
    for level in range(0, max_shyness+1):
        current_amount = int(auditory[level])
        if current_amount > 0 and total < level:
            needed += level - total
            total += level - total
        total += current_amount
    out.write("Case #{0}: {1}\n".format(case, str(needed)))
    case += 1
