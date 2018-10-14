#!/usr/bin/env python
#coding=utf8
from code_jam.bios import CaseSolverInterface, CaseInterface

__author__ = 'mnach'


class Case(CaseInterface):
    def __init__(self):
        self.first_answer = self.second_answer = 0
        self.first = list()
        self.second = list()

    def solve(self):
        first = self.first[self.first_answer - 1].copy()
        second = self.second[self.second_answer - 1].copy()
        answer = [i for i in first if second.count(i)]
        if len(answer) > 1:
            return 'Bad magician!'
        elif not len(answer):
            return 'Volunteer cheated!'
        else:
            return answer[0]

    def append(self, line):
        if not self.first_answer:
            self.first_answer = int(line.strip())
        elif len(self.first) < 4:
            self.first.append([int(i) for i in line.strip().split()])
        elif not self.second_answer:
            self.second_answer = int(line.strip())
        elif len(self.second) < 4:
            self.second.append([int(i) for i in line.strip().split()])
            if len(self.second) == 4:
                return True


class CaseSolver(CaseSolverInterface):
    def load(self, line):
        if not self.is_init():
            return self.init(line, Case)
        ret = self._case.append(line)
        if ret:
            self._case_num += 1
        return ret