#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

input_file = open(sys.argv[1])
if len(sys.argv) > 2:
    output_file = open(sys.argv[2], 'w')

class Invoke:
    def __init__(self, combines, opposes):
        self.combines = {}
        for combine in combines:
            combo = combine[:2]
            replace = combine[-1]
            self.combines[combo] = replace
            self.combines[combo[::-1]] = replace

        self.opposes = {}
        for oppose in opposes:
            oppA, oppB = tuple(oppose)
            if self.opposes.get(oppA):
                self.opposes[oppA].add(oppB)
            else:
                self.opposes[oppA] = {oppB}
            if self.opposes.get(oppB):
                self.opposes[oppB].add(oppA)
            else:
                self.opposes[oppB] = {oppA}

    def invoke(self, invoke_list):
        self.queue = ''
        for element in invoke_list:
            self.queue += element
            last_two = self.queue[-2:]
            if last_two in self.combines:
                self.queue = self.queue[:-2] + self.combines[last_two]
            elif self.opposes.get(element, set()).intersection(self.queue):
                self.queue = ''

    def __str__(self):
        return '[' + ', '.join('{}'.format(elem) for elem in self.queue) + ']'


def parse(line):
    C, *seq, N, invoke_list = line.split()
    C, N = int(C), int(N)
    combines, D, opposes = seq[:C], seq[C], seq[C + 1:]

    return combines, opposes, invoke_list


def solve(line):
    combines, opposes, invoke_list = parse(line)

    invoke = Invoke(combines, opposes)
    invoke.invoke(invoke_list)

    return invoke

cases = int(next(input_file))

for case in range(1, cases + 1):
    print('Case #{case}: {result}'.
          format(case=case, result=solve(next(input_file))),
          file=output_file if len(sys.argv) > 2 else sys.stdout, )
