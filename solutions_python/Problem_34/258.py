#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from base import GcjSolver

class AlienSolver(GcjSolver):
    def run(self):
        self.fin = open(self.name_in, "r")
        self.fout = open(self.name_out, "w")

        L, D, N = [int(x) for x in self.get_line().split(' ')]
        self.words = {}
        for i in xrange(D):
            self.words[self.get_line()] = True
        self.letters_at = [[] for x in xrange(L)]

        for word in self.words:
            for index, c in enumerate(word):
                self.letters_at[index].append(c)

        for i in xrange(N):
            case = self.get_case()
            answer = self.solve(case)
            self.write(i, answer)
        self.fin.close()
        #print "Done"

    def get_case(self):
        line = self.get_line()
        return line
    def solve(self, line):
        self.count = 0
        for word in self.words:
            #print "Checking if word %s matches pattern %s" % (word, line)
            self.check(word, line)
            #print "*"*40
        return self.count

    def check(self, word, line):
        sets = self.parse(line)
        flag = True
        for index, c in enumerate(word):
            if c in sets[index]:
                pass
                #print c, "is in", sets[index]
            else:
                flag = False
        if flag:
            self.count += 1
    def parse(self,line):
        new_line = ""
        in_parenthesis = False
        for c in line:
            if c == "(":
                new_line += c
                in_parenthesis = True
            elif c == ")":
                new_line += c
                in_parenthesis = False
            else:
                if in_parenthesis:
                    new_line += c
                else:
                    new_line += "("+c+")"
        line = new_line
        lista = line.replace("(","|").replace(")","|").split("|")
        lista2 = []
        for x in lista:
            if x != '':
                lista2.append(x)
        return lista2

def main(program, name):
    s = AlienSolver(name)
    s.run()


if __name__ == '__main__':
    reload(sys); sys.setdefaultencoding('utf-8')
    main(*sys.argv)