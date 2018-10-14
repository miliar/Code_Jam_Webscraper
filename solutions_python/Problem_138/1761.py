#!/usr/bin/env python

import re
import sys

outf = 'out.txt'
inf = 'D-large.in.txt'

class Player(object):

    def __init__(self, op=None):
        self.cards = []
        self.score = 0
        # opponent
        self.op = op

    def scores(self):
        self.score += 1

    def read_cards(self, cs):
        self.cards = sorted(cs)

    def test_print(self):
        print self.cards


class FirstPlayer(Player):

    def play_war(self):
        return self.cards.pop(-1)

    def play_dwar(self):
        if self.cards[0] > self.op.cards[-1]:
            return self.play_war()
        elif self.cards[-1] < self.op.cards[0]:
            return self.play_war()
        elif self.cards[-1] > self.op.cards[-1]:
            if self.op.cards[0] < self.cards[0] < self.op.cards[-1]:
                t = self.op.cards[-1] + 1
                self.cards.pop(0)
                return t
            else:
                t = (self.op.cards[-1] + self.op.cards[-2]) / 2
                self.cards.pop(0)
                return t
        elif self.cards[-1] < self.op.cards[-1]:
            if self.op.cards[0] < self.cards[0] < self.op.cards[-1]:
                t = self.op.cards[-1] + 1
                self.cards.pop(0)
                return t
            else:
                t = (self.op.cards[-1] + self.op.cards[-2]) / 2
                self.cards.pop(0)
                return t


class LastPlayer(Player):

    def nc_idx(self, oc):
        """
        Parameters
        ----------
        oc: float
            Told card by opponent.
        """
        widx = filter(lambda x: self.cards[x] > oc, range(len(self.cards)))
        if len(widx) > 0:
            return widx[0]
        else:
            return 0

    def reveal_card(self, oc):
        nc_idx = self.nc_idx(oc)
        return self.cards[nc_idx]

    def play_war(self, oc):
        nc_idx = self.nc_idx(oc)
        return self.cards.pop(nc_idx)


class Game(object):

    def __init__(self, p0, p1, n):
        self.p = []
        self.p.append(p0)
        self.p.append(p1)
        self.n = n

    def judge(self, c0, c1):
        if c0 > c1:
            self.p[0].scores()
        else:
            self.p[1].scores()


class WarGame(Game):

    def play(self):
        for i in range(self.n):
            c0 = self.p[0].play_war()
            c1 = self.p[1].play_war(c0)
            self.judge(c0, c1)


class DWarGame(Game):

    def play(self):
        for i in range(self.n):
            c0 = self.p[0].play_dwar()
            c1 = self.p[1].play_war(c0)
            self.judge(c0, c1)


def read_and_solve(pid, fo, fi):
    n = int(fi.readline())

    ken0 = LastPlayer()
    naomi0 = FirstPlayer()
    ken1 = LastPlayer()
    naomi1 = FirstPlayer(op=ken1)

    cards = [float(x) for x in re.split(r'\s+', fi.readline().strip())]
    naomi0.read_cards(cards)
    naomi1.read_cards(cards)
    cards = [float(x) for x in re.split(r'\s+', fi.readline().strip())]
    ken0.read_cards(cards)
    ken1.read_cards(cards)

    wg = WarGame(naomi0, ken0, n)
    dwg = DWarGame(naomi1, ken1, n)

    wg.play()
    dwg.play()
    string = "Case #" + str(pid) + ": " + \
            str(naomi1.score) + " " + str(naomi0.score) + "\n"
    fo.write(string)


def main():
    fi = open(inf, 'rU')
    with open(outf, 'w') as fo:
        n = int(fi.readline().strip())
        ndone = 0
        while ndone < n:
            try:
                # 1-based numbering
                read_and_solve(ndone + 1, fo, fi)
                ndone += 1
            except EOFError:
                break
    fi.close()


if __name__ == "__main__":
    main()
