__author__ = 'pablo'

lines = open('A-large.in').read().splitlines()
f = open('out.txt', 'w')


def solve(max, numbers):
    if max == 0:
        return 0

    count = 0
    acc = numbers[0]
    for shyness in range(1, len(numbers)):
        if (shyness > acc):
            count = count + shyness - acc
            acc = acc + shyness - acc
        acc = acc + numbers[shyness]
    return count


for i in range(1, len(lines)):
    line = lines[i].split(' ')
    numbers = [int(n) for n in line[1]]
    #print numbers
    f.write("Case #%d: %d\n" % (i, solve(int(line[0]), numbers)))
