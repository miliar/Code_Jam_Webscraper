import math as m
import numpy as np
import sys
import collections as clc


Pancake = clc.namedtuple("Pancake", ("radius", "height"))

def lost_area(pile, index):
    if index is 0:
        if len(pile) is 1:
            return pile[0].radius*(pile[0].radius+2*pile[0].height)
        if len(pile) > 1:
            return 2*pile[0].radius*pile[0].height + pile[0].radius**2 - pile[1].radius**2
    return 2*pile[index].height*pile[index].radius

def compute_area(pile):
    return (pile[0].radius**2 + sum([2*pancake.height*pancake.radius for pancake in pile]))*m.pi


if __name__ == "__main__":
    filename = sys.argv[1]
    infile = open(filename+".in", "r")
    outfile = open(filename+".out", "w")
    T = int(infile.readline())
    for case in range(T):
        N, K = [int(num) for num in infile.readline().split()]
        pile = list()
        for n in range(N):
            radius, height = [int(num) for num in infile.readline().split()]
            pancake = Pancake(radius, height)
            if len(pile) is 0:
                pile.append(pancake)
            else:
                index = len(pile)
                while index > 0 and radius > pile[index-1].radius:
                    index -= 1
                pile.insert(index, pancake)
        print pile
        for k in range(N-K):
            areas_to_lose = [lost_area(pile, index) for index in range(len(pile))]
            pancake_to_remove = np.argmin(areas_to_lose)
            pile.pop(pancake_to_remove)
        print pile
        area = compute_area(pile)
        outfile.write("Case #{}: {}\n".format(case+1, area))
    infile.close()
    outfile.close()
