#!/usr/bin/env python

from parallels import par

class ProblemA:
    def __init__(self):
        self.tab = []
        self.R, self.C = None, None
    def read(self):
        self.R, self.C = map(int,raw_input().split())
        for r in range(self.R):
            self.tab.append(raw_input())
    def solve(self):
        summa = 0
        possible = True
        for r in range(self.R):
            for c in range(self.C):
                if self.tab[r][c]!='.':
                    ok = {'^':False,'>':False,'v':False,'<':False}
                    for xx in range(r):
                        if self.tab[xx][c]!='.':
                            ok['^'] = True
                    for xx in range(c):
                        if self.tab[r][xx]!='.':
                            ok['<'] = True
                    for xx in range(r+1,self.R):
                        if self.tab[xx][c]!='.':
                            ok['v'] = True
                    for xx in range(c+1,self.C):
                        if self.tab[r][xx]!='.':
                            ok['>'] = True
                    if not (ok['v'] or ok['<'] or ok['^'] or ok['>']):
                        possible = False
                    elif self.tab[r][c]=='<' and not ok['<']:
                        summa += 1
                    elif self.tab[r][c]=='^' and not ok['^']:
                        summa += 1
                    elif self.tab[r][c]=='>' and not ok['>']:
                        summa += 1
                    elif self.tab[r][c]=='v' and not ok['v']:
                        summa += 1
        if not possible:
            return 'IMPOSSIBLE'
        else:
            return summa

if __name__ == '__main__':
    par.seq(ProblemA)