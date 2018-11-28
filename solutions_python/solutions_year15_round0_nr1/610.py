import re
import sys


def parse(f):
    S_max, people = f.readline().strip().split()

    return int(S_max), map(int, re.findall(".", people))


def solve(S_max, people):
    result, standing, total = 0, 0, sum(people)

    while True:
        for i, p in enumerate(people):
            if standing >= i:
                standing += p

        if standing == total:
            break
        else:
            result += 1
            total += 1
            standing = result

    return result
    

def main():
    with open(sys.argv[1], "r") as input_file:
        T = int(input_file.readline())

        for i in xrange(T):
            S_max, people = parse(input_file)
            result = solve(S_max, people)

            print "Case #%d: %d" % (i+1, result)


if __name__ == "__main__":
    main()
