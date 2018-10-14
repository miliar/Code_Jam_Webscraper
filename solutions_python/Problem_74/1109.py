#! /usr/bin/python3

import argparse, csv
from Bot import Bot, go_push_the_buttons

parser = argparse.ArgumentParser(description='Problem A - Bot Trust from Google Code Jam')
parser.add_argument('input', help='the input file given by the code jam website')
args = parser.parse_args()

with open(args.input, newline='') as f:
    reader = csv.reader(f, delimiter=' ')
    test_number = next(reader)[0]

    # for each test
    for i in range(int(test_number)):
        test = next(reader)
        test.reverse()
        actions_number = test.pop()
        actions = []

        # parse the targets' line
        for j in range(int(actions_number)):
            actions.append((test.pop(), int(test.pop())))

        go_push_the_buttons(i+1, actions)
