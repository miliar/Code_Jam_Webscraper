import sys

def solve_problem(smax, people):
    stoodup = 0
    need_more = 0
    for level, num_of_people in enumerate(people):
        if level > stoodup:
            more = level - stoodup
            stoodup += more
            need_more += more
        stoodup += int(num_of_people)
    return need_more

if __name__ == "__main__":
    num_of_cases = int(sys.stdin.readline().strip())

    for i in xrange(1, num_of_cases + 1):
        smax, people = sys.stdin.readline().split()
        print "Case #{0}: {1}".format(i, solve_problem(int(smax), people))
