#!/usr/bin/env python

import argparse

def main():
    parser = argparse.ArgumentParser(description="A. Bot Trust")
    parser.add_argument("filename")
    parser.add_argument("--pudb", action="store_true")
    args = parser.parse_args()

    if args.pudb:
        import pudb
        pudb.set_trace()

    f = open(args.filename)
    s = f.readlines()
    f.close()

    # number of test cases
    t = int(s[0])
    cases = {}
    for i in range(1, len(s)):
        cases[i] = s[i].replace('\n','')
    for i in sorted(cases.keys()):
        print "Case #{0}: {1}".format(i, solve(cases[i].split(' ')))

def solve(case):
    # number of buttons to push
    n = int(case[0])
    case = case[1:]
    # instructions
    buttons = []
    for i in range(n):
        # take the first character off, grab new first character
        bot = case[0]
        case = case[1:]
        button = int(case[0])
        case = case[1:]
        buttons.append(Button(bot, button))

    # positions
    b_position = 1
    o_position = 1
    elapsed_time = 0
    while len(buttons) > 0:
        o_used = False
        b_used = False

        next_bot = buttons[0].bot
        o_goal = find_first_of(buttons, 'O', o_position)
        b_goal = find_first_of(buttons, 'B', b_position)
        
        # attempt to move toward next goal
        if b_position < b_goal:
            b_position += 1
            b_used = True
        elif b_position > b_goal:
            b_position -= 1
            b_used = True
        if o_position < o_goal:
            o_position += 1
            o_used = True
        elif o_position > o_goal:
            o_position -= 1
            o_used = True

        # if it's your turn, and you're on target, push
        if b_position == b_goal and next_bot == "B" and not b_used:
            buttons = buttons[1:]
        elif o_position == o_goal and next_bot == "O" and not o_used:
            buttons = buttons[1:]

        # 1 second has passed.
        elapsed_time += 1
    
    return elapsed_time


def find_first_of(buttons, bot, cur_pos):
    for b in buttons:
        if b.bot == bot:
            return b.n
    return cur_pos

class Button(object):
    def __init__(self, bot, n):
        self.bot = bot
        self.n = n

if __name__=="__main__":
    main()
