#!/usr/bin/env python
# vim:fileencoding=utf-8

import sys
import pprint

pp = pprint.PrettyPrinter(indent=4)

ntest = 0
inputs = []

def solve():
    for n in range(ntest):
        first_ans = inputs[n]["first_answer"] - 1
        second_ans = inputs[n]["second_answer"] - 1
        result = set(inputs[n]["first"][first_ans]).intersection(set(inputs[n]["second"][second_ans]))
        # print result
        l = len(result)
        print "Case #{0}:".format(n+1),
        if l == 1:
            print result.pop()
        elif l > 1:
            print "Bad magician!"
        else:
            print "Volunteer cheated!"


def parse():
    global ntest
    global inputs
    ntest = int(sys.stdin.readline().strip())
    for n in range(ntest):
        first = []
        second = []
        first_answer = int(sys.stdin.readline().strip())
        for i in range(4):
            first.append([int(j) for j in sys.stdin.readline().strip().split(" ")])
        second_answer = int(sys.stdin.readline().strip())
        for i in range(4):
            second.append([int(j) for j in sys.stdin.readline().strip().split(" ")])
        inputs.append({"first_answer": first_answer,
                       "first": first,
                       "second_answer": second_answer,
                       "second": second})
    # pp.pprint(inputs)

if __name__ == '__main__':
    parse()
    solve()
