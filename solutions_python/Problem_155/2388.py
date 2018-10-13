#!/usr/bin/env python
import sys

'''https://code.google.com/codejam/contest/6224486/dashboard'''
from runner import CodeJamRunner

def solution(smax, shyness):
    # print "smax:%s shyness:%s" % (smax, shyness)
    stands = 0
    invites = 0
    for i, n in enumerate(shyness):
        n = int(n)
        # print "i:%s n:%s stands %s invites:%s" % (i, n, stands, invites)
        if stands >= shyness:
            break
        new_invites = 0
        if i > stands and n > 0:
            new_invites = i - stands
            # if new_invites < 0: new_invites = 0
            invites += new_invites
        stands += n + new_invites

    # print "invites: %s" % invites
    return invites


class SolutionRunner(CodeJamRunner):

    def read_test(self, f):
            line = f.readline()
            (smax, shyness) = line.split(" ")
            return {
                'smax': smax,
                'shyness': shyness.strip()
                }

    def execute(self, **kwargs):
        return solution(**kwargs)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.stderr.write('Use %s <filename>\n' % sys.argv[0])
        sys.exit(1)
    runner = SolutionRunner(sys.argv[1])
    runner.print_result()
