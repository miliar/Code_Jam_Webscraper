#!/usr/bin/env python
#

from sets import Set

class App(object):
    def __init__(self, inf, outf):
        self.infname = inf
        self.outfname = outf

    def report(self, c, r):
        if r < 1:
            rs = ("", "Bad magician!", "Volunteer cheated!")[-r]
        else:
            rs = str(r)

        self.outf.write("Case #{}: {}\n".format(c, rs))

    def draw(self):
        ans = int(self.inf.readline())
        cards = [ [], [], [], [] ]

        for row in range(4):
            cards[row] = map(int, self.inf.readline().split())
        return ans, cards

    def run_case(self, c):
        ans1, cards1 = self.draw()
        set1 = Set(cards1[ans1 - 1])

        ans2, cards2 = self.draw()
        set2 = Set(cards2[ans2 - 1])

        r = -2
        for m1 in set1:
            if m1 in set2:
                if r > 0:
                    r = -1
                    break
                r = m1

        self.report(c, r)

    def run(self):
        self.inf = open(self.infname, "r")
        self.outf = open(self.outfname, "w")

        ncases = int(self.inf.readline())

        for c in range(ncases):
            self.run_case(c + 1)

        self.inf.close()
        self.outf.close()


if __name__ == "__main__":
    App("./A-small-0.in", "A-small-0.out").run()

