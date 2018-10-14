
import logging
import os
import sys

import argparse


class Case(object):
    def __init__(self, n, S, K):
        self.n = n
        self.S = S
        self.K = K
        self.r = 'IMPOSSIBLE'

    def solve(self):
        logging.debug('solving for #%d ...', self.n)

        pancakes = int(self.S.replace('+', '1').replace('-', '0'), 2)
        flipper = int('1' * int(self.K), 2)
        all_happy = int('1' * len(self.S), 2)
        offset = len(self.S) - int(self.K)

        logging.debug('pancakes=0b%s, flipper=0b%s', bin(pancakes), bin(flipper))

        def analyse(n, current_states, all_states):
            logging.debug('analysing n=%d, current_states=%s, all_states=%s',
                          n,
                          ','.join(['0b{0:b}'.format(s) for s in current_states]),
                          ','.join(['0b{0:b}'.format(s) for s in all_states]))

            # check if we have a valid result
            if all_happy in current_states:
                return n

            states0 = set()
            for s in current_states:
                for o in range(0, offset+1):
                    # flip pancakes at offset
                    s0 = (s >> o) ^ flipper
                    # re-combine state at offset
                    s1 = (s0 << o) + (s % (2 ** o))
                    # add to combination of states
                    states0.add(s1)

            # impossible when no new states are found
            if len(states0 - all_states) == 0:
                return self.r

            return analyse(n+1, states0, all_states | states0)

        self.r = analyse(0, {pancakes}, {pancakes})

    @property
    def result(self):
        return 'Case #{0}: {1}'.format(self.n, self.r)


parser = argparse.ArgumentParser()
parser.add_argument('--output-file', default=None)
parser.add_argument('input_file', nargs=1)
arguments = parser.parse_args()

logging.basicConfig(level=logging.DEBUG)

output = sys.stdout if arguments.output_file is None else open(arguments.output_file, 'w')

with open(arguments.input_file[0]) as input_file:
    T = int(input_file.readline().strip())
    for i, l in enumerate(input_file):
        c = Case(i+1, *l.split(' '))
        c.solve()
        output.write(c.result)
        output.write(os.linesep)
