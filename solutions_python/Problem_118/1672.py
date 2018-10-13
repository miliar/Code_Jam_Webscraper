import sys, itertools, math

lines_per_case = 1

def is_palim(s):
    if len(s) <= 1:
        return True
    elif s[0] == s[-1]:
        return is_palim(s[1:-1])
    return False
        

palims = []

# precompute all fair palindromes for < 1000
for i in range(0, 10**7):
    sq = int(math.pow(i, 2))
    if is_palim(str(i)) and is_palim(str(sq)):
        palims.append(sq)

def solve_case(case):
    low, high = map(int, case.split())
    counter = 0

    for p in palims:
        if low <= p <= high:
            counter += 1
        if p > high:
            break

    return str(counter)


def produce_output(index, solution):
    print 'Case #%s: %s' % (index, solution)


if __name__ == "__main__":
    if(len(sys.argv) > 1):
        fn = sys.argv[1]
        with open(fn) as f:
            lines = f.readlines()
            nt = int(lines[0])
            for index, case in enumerate(lines[1:], 1):
                solution = solve_case(case)
                produce_output(index, solution)
