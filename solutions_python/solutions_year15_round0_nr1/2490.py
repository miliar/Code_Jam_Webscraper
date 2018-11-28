__author__ = 'jerome'


# -*- coding: utf8 -*-


import sys


def resolve_exo1(nb, shyness_level):
    total_friends_needed = 0
    clapping = int(shyness_level[0])
    for i in range(1, nb+1):
        if i > clapping:
            friend_needed = i - clapping
            total_friends_needed += friend_needed
            clapping += friend_needed
        clapping += int(shyness_level[i])

    return total_friends_needed

if __name__ == '__main__':

    lines = []

    for line in sys.stdin:
        lines.append(line.rstrip('\n'))

    for i in range(1, int(lines[0])+1):
        nb, shyness_level = lines[i].split(" ")
        print("Case #{0}: {1}".format(i, resolve_exo1(int(nb), shyness_level)))