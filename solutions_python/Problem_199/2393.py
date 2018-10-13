import sys

def parse_pancakes(line, width):
    flips = 0
    for i in range(len(line) - width + 1):
        if line[i] == '-':
            # flip
            for j in range(width):
                if line[i+j] == '-':
                    line[i+j] = '+'
                else:
                    line[i+j] = '-'
            flips += 1
    if all([p == '+' for p in line]):
        return flips
    else:
        return "IMPOSSIBLE"


def main():
    # Parse the test file and generate output
    # Discard first line
    sys.stdin.readline()

    case = 1
    for line in sys.stdin:
        line = line.strip()
        if line:
            width = int(line.split()[1])
            line = [l for l in line.split()[0]]
            result = parse_pancakes(line, width)
            print "Case #%d: %s" % (case, result)
            case += 1


if __name__ == '__main__':
    main()
