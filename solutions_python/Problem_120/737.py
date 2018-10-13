def read(filename):
    input = open(filename, 'r')
    lines = []
    for line in input:
        lines.append(line.rstrip('\n')) # strip out the newline characters
    return lines

def circle(r, t):
    num = 0
    amount_used = 0
    r += 1
    while amount_used <= t:
        area = (2 * r - 1)
        amount_used += area
        num += 1
        r += 2
    return num - 1


def main():
    lines = read('A-small-attempt0.in')
    num = int(lines.pop(0))
    line_num = 0
    for i in range(num):
        line = lines[i].split()
        r, t = int(line[0]), int(line[1])
        print("Case #" + str(i + 1) + ": " + str(circle(r, t)))
        line_num += 1

if __name__ == '__main__':
    main()
