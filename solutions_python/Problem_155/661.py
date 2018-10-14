import sys


def solve_case(audiences, case_number):
    friends = 0
    standing_audiences = 0
    for i, audience in enumerate(map(int, audiences)):
        need_friends = 0
        if i > standing_audiences:
            need_friends = i - standing_audiences
        standing_audiences += (audience + need_friends)
        friends += need_friends

    print "Case #%d: %d" % (case_number, friends)


#main
if __name__ == '__main__':
    r = sys.stdin

    if len(sys.argv) > 1:
        r = open(sys.argv[1], 'r')

    total_cases = r.readline()
    for cn in range(1, int(total_cases) + 1):
        solve_case(r.readline().strip().split()[1], cn)

