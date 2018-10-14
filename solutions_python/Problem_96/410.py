#! /usr/bin/python
# Martin Pool
# https://code.google.com/codejam/contest/1460488/dashboard#s=p1

from sys import stdin

# For any total score T, we can calculate all the (fairly small) possible
# combinations of scores that would produce that total; basically all within
# T/3 +/- 2.  More specifically we can calculate both some combinations that
# are unsurprising, some that are surprising, and we can leave aside the
# rest, which are impossible...
#
# We only need to worry about combinations; ordering between the judges
# doesn't matter; we might as well give them in descending order.
#
# Looking at these we can say whether it's possible they got an unsurprising
# result with a score over p, or whether they could have got that only by
# having a surprising result.
#
# Then the maximum number of scores over p will be if we use all the
# surprising scores where that helps.
#
# Ignoring ordering, there's actually only one unsurprising panel per score.
#

def unsurprising_panel(total):
    a = total // 3
    if total % 3 == 2:
        return (a+1, a+1, a)
    elif total % 3 == 1:
        return (a+1, a, a)
    else:
        return (a, a, a)


def unsurprising_best(total):
    return unsurprising_panel(total)[0]


# The most interesting surprising panel is where the highest judge (if any)
# is pushed up and the second highest is pushed down.  (But, we must never
# push above 10 or below 0.)  This is most interesting because it's
# most likely to put their best score over p.  We can only do this if the gap
# between them is currently 0, otherwise moving one point will put them more 
# than two points apart.

def surprising_best(total):
    p = unsurprising_panel(total)
    if p[0] >= 10:
        # Can't push it further up
        return p[0]
    elif p[0] != p[1]:
        # Already 1 point apart; can't borrow one or they'd be 3 points
        # apart.
        return p[0]
    elif p[1] > 0:
        # Take one from here, add to the first judge.
        return p[0] + 1
    else:
        # Can't borrow anything, remains stuck at 1 or 0.
        return p[0]


# If we have S surprising results, we will use them up on the first S trials
# where that would make any difference: ie where the dancer could not have
# been above P without a surprised, but could if we do have a surprise.
def find_maximum(num_surprises, goal_score, total_list):
    possible_qualifiers = 0
    for dancer_total in total_list:
        if unsurprising_best(dancer_total) >= goal_score:
            possible_qualifiers += 1
        elif num_surprises > 0:
            if surprising_best(dancer_total) >= goal_score:
                possible_qualifiers += 1
                num_surprises -= 1
    return possible_qualifiers


# Read and process input
num_cases = int(stdin.readline())
for i_case in range(num_cases):
    case_fields = map(int, stdin.readline().rstrip("\n").split())
    num_dancers, num_surprises, goal_score = case_fields[0:3]
    total_list = case_fields[3:]
    assert len(total_list) == num_dancers
    print 'Case #%d: %d' % (i_case + 1,
            find_maximum(num_surprises, goal_score, total_list))
    

# tests
assert unsurprising_panel(30) == (10, 10, 10)
assert unsurprising_panel(24) == (8, 8, 8)
assert unsurprising_panel(22) == (8, 7, 7)
assert unsurprising_panel(2) == (1, 1, 0)
assert unsurprising_panel(7) == (3, 2, 2)


assert surprising_best(0) == 0
assert surprising_best(1) == 1
assert surprising_best(2) == 2
assert surprising_best(3) == 2
assert surprising_best(4) == 2
assert surprising_best(5) == 3
assert surprising_best(6) == 3
assert surprising_best(7) == 3
assert surprising_best(8) == 4
assert surprising_best(9) == 4
assert surprising_best(10) == 4

assert find_maximum(1, 5, [15, 13, 11]) == 3
assert find_maximum(0, 8, [23, 22, 21]) == 2
assert find_maximum(1, 1, [8, 0]) == 1
assert find_maximum(2, 8, [29, 20, 8, 18, 18, 21]) == 3
