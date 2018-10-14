
import sys

def roller_coaster(R, k, N, groups):
    total = 0
    for r in range(R):
        in_roller = []
        current = 0
        while groups:
            next = groups[0]
            if current + next <= k:
                in_roller.append(groups.pop(0))
                current += next
            else:
                break
        total += current
        groups.extend(in_roller)
    return total


if __name__ == '__main__':
    stdin = sys.stdin
    num_cases = stdin.readline()

    for i in range(int(num_cases)):
        line = stdin.readline()
        R, k, N = map(int, line.split())
        line = stdin.readline()
        groups = map(int, line.split())

        total = roller_coaster(R, k, N, groups)

        print "Case #%d: %d" % (i+1, total)
