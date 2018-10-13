#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


def solve():
    # read problem
    smax, audience = readlist()
    smax = int(smax)
    audience = [int(shy) for shy in audience]

    friends = 0
    standing = 0
    for shyness, people in enumerate(audience):
        if standing >= shyness:
            # all these people stand up
            standing += people
        else:
            # invite friends
            new_friends = shyness - standing
            friends += new_friends
            # then they'll stand up, as well as the newly invited friends
            standing += people + new_friends

    answer = friends
    return answer


def format_answer(answer):
    return answer




#####################################
## Boilerplate
import fileinput

def read(typ=str, lines=fileinput.input()):
    return typ(lines.readline().strip())

def readlist(typ=str):
    return [typ(item) for item in read(str).split()]

def main():
    t = read(int)
    for case in range(1, 1+t):
        answer = solve()
        print("Case #{}: {}".format(case, format_answer(answer)))

if __name__ == "__main__":
    main()

