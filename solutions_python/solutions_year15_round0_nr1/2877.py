#!/usr/bin/env python

import sys

INPUT_FILE = "input.txt"

def main():

    with open(INPUT_FILE, "r") as f:
        cases = int(f.readline())

        for i in range(cases):
            line = f.readline().rstrip().split()
            s_max = int(line[0])
            s_count = [int(i) for i in list(line[1])]

            result = how_many_friends(s_max, s_count)

            print("Case #%d: %d" % (i+1, result))

def how_many_friends(s_max, counts):
    """
    s_max = shyness level of most shy person in audience
    counts = counts of how shy people are, where count[i] is the count
      of people with shyness i


    return the number of friends you need to bring with you

    """
    friends = 0
    standing = 0

    for s in range(len(counts)):
        """
        There are counts[s] people with shyness level s in the audience
        These will stand if there are at least s people standing.
        If there are fewer than s people standing, bring the difference
          as friends who will stand.
        """
        if standing < s:
            diff = s - standing
            friends = friends + diff
            standing = standing + diff
        standing = standing + counts[s]

    return friends

if __name__ == "__main__":
    main()
