# Exercise 1: Standing Ovation
import sys


def main(*args):
    lines = [line.strip() for line in sys.stdin]
    it = iter(lines)
    num_cases = int(it.next())
    for case_no in range(num_cases):
        try:
            output = run_case(it.next())
            if type(output) == list or type(output) == tuple:
                output = ' '.join(output)
            print("Case #%d: %s" % (case_no + 1, output))
        except StopIteration, e:
            print("Error: End of input.")


def run_case(case):
    audience = case.split(' ')[1]

    count = int(audience[0])
    res = 0
    for i in range(1, len(audience)):
        if count < i:
            if audience[i] != 0:
                while count < i:
                    count += 1
                    res += 1
        count += int(audience[i])

    return res

if __name__ == '__main__':
    main(*sys.argv[1:])
