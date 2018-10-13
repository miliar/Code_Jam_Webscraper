#!/usr/bin/python

class guess:
    def __init__(self, input_file):
        self.g = int(input_file.readline())
        self.p = []
        for _ in range(4):
            self.p.append( map(int, input_file.readline().split()))

    def possible_answers(self):
        return self.p[self.g - 1]

def solve_n(case, input_file):
    f = guess(input_file)
    f_p = set(f.possible_answers())
    s = guess(input_file)
    s_p = set(s.possible_answers())

    r = set.intersection(f_p, s_p)

    if len(r) == 1:
        res = list(r)[0]
    elif len(r) == 0:
        res = "Volunteer cheated!"
    else:
        res = "Bad magician!"

    print "Case #%d: %s" % (case, res)


def solve(input_file):
    n = int(input_file.readline())
    for case in range(n):
        solve_n(case + 1, input_file)

if __name__ == "__main__":
    import sys
    solve(open(sys.argv[1],"r"))

