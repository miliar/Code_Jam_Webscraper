#!/usr/bin/env python3
"""Google Code Jam Submission
Problem: 2011 Round 1C Problem B
Author: Matt Giuca
"""

import sys

### Input parsing ###

def parse_input(infile):
    """Consume input for a single case from infile.
    Return or yield a data structure describing the input.
    """
    ints = list(map(int, infile.readline().strip().split()))
    l = ints[0]
    t = ints[1]
    n = ints[2]
    c = ints[3]
    a = ints[4:]
    assert c == len(a)
    return l, t, n, a

### Algorithm ###

def calculate_q_star(t, a):
    """Calculate which star we will have just left when boosters go live.
    If boosters go live WHILE we are at a star, that is q_star.
    Also return hours into q_star when we go live (>= 0).
    """
    time_per_c_cycle = sum(a) * 2
    num_full_c_cycles = t // time_per_c_cycle
    result = num_full_c_cycles * len(a)
    hours_in = 0
    remaining_time = t % time_per_c_cycle
    for dist in a:
        if remaining_time < dist*2:
            hours_in = remaining_time
            break
        remaining_time -= dist*2
        result += 1
    return result, hours_in

def build_stars(n, a):
    for i in range(n):
        yield a[i%len(a)]

def set_boosters(stars, q_star, hours_in, allow_boost_on_q_star, l, a):
    """Takes a list of distances; returns a list of speeds."""
    speeds = [x*2 for x in stars]
    a = sorted(a)
    i = len(stars)-1
    boost_on_dist = a.pop()
    while l > 0:
        while ((i > q_star or (i == q_star and allow_boost_on_q_star))
            and stars[i] != boost_on_dist):
            i -= 1
        if i < q_star or (i == q_star and not allow_boost_on_q_star):
            if len(a) == 0:
                break
            i = len(stars)-1
            boost_on_dist = a.pop()
            continue
        if i == q_star:
            dist_in = hours_in // 2
            speeds[i] = dist_in*2 + (stars[i]-dist_in)
        else:
            speeds[i] = stars[i]
        l -= 1
        i -= 1
    return speeds

def handle_case(data):
    """Given the data structure returned by parse_input, return the answer as
    a string or stringable value.
    If parse_input is a generator, should manually call list() on data.
    """
    l, t, n, a = data
    q_star, hours_in = calculate_q_star(t, a)
    stars = list(build_stars(n, a))
    # Try not allowing a boost on q_star
    speeds = set_boosters(stars, q_star, hours_in, False, l, a)
    score_not_allow_q = sum(speeds)
    # Try allowing a boost on q_star
    speeds = set_boosters(stars, q_star, hours_in, True, l, a)
    score_allow_q = sum(speeds)
    #print("score_not_allow_q = {0}, score_allow_q = {1}".format(score_not_allow_q, score_allow_q))
    return min(score_not_allow_q, score_allow_q)

### Top-level ###

def main():
    numcases = int(sys.stdin.readline())
    for casenum in range(numcases):
        data = parse_input(sys.stdin)
        answer = handle_case(data)
        print("Case #{0}: {1}".format(casenum+1, answer))

if __name__ == "__main__":
    sys.exit(main())
