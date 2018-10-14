#!/usr/bin/env python
#

from sets import Set

class App(object):
    def __init__(self, inf, outf):
        self.infname = inf
        self.outfname = outf

    def report(self, c, r):
        pass

    def run_case(self, case):
        c, f, x = map(float, self.inf.readline().split())

        time = 0.0
        cookies = 0.0
        rate = 2.0

        while True:
            needed = x - cookies
            if needed < c:
                time += (needed / rate)
                break

            time += ((c - cookies) / rate)
            cookies = c
            needed = x - cookies

            nobuy = needed / rate
            buy = x / (rate + f)

            if nobuy < buy:
                time += (needed / rate)
                break

            cookies = 0.0
            rate += f

        self.outf.write("Case #{:d}: {:.7f}\n".format(case, time))


    def run(self):
        self.inf = open(self.infname, "r")
        self.outf = open(self.outfname, "w")

        ncases = int(self.inf.readline())

        for c in range(ncases):
            self.run_case(c + 1)

        self.inf.close()
        self.outf.close()


if __name__ == "__main__":
    App("./B-large.in", "B-large-0.out").run()

