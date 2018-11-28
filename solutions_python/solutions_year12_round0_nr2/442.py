import sys


def find_p(surprising, p, googlers):
    counter = 0

    for vote_sum in googlers:
        if p == 0:
            counter += 1
        elif vote_sum >= 3 * p - 2 and p - 1 >= 0:
            counter += 1
            #print vote_sum, "is not surprising but has high score!"

        elif vote_sum >= 3 * p - 4 and surprising > 0 and p - 2 >= 0:
            #print vote_sum, "is surprising and hs high score!"
            counter += 1
            surprising -= 1

    return counter


with open(sys.argv[1]) as f:
    n_cases = f.readline()
    cases = [map(int, line.split(" ")) for line in f]

for i, case in enumerate(cases):
    n, s, p = case[:3]
    googlers = case[3:]

    print "Case #%d: %s" % (i + 1, find_p(s, p, googlers))
