#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


def standing_ovation(path):
    
    with open(path) as f:
        content = f.readlines()
    t = int(content[0].replace("\n", ""))
    for i in range(1, t+1):
        line = content[i].replace("\n", "").split(" ")
        smax = int(line[0])
        si = [0] * (smax + 1)
        for j, sj in enumerate(line[1]):
            si[j] = int(sj)

        people_to_add = 0
        people_standing_up = 0
        for shyness_level in range(0, smax + 1):
            if si[shyness_level] > 0 and people_standing_up >= shyness_level:
                people_standing_up += si[shyness_level]
            elif si[shyness_level] > 0:
                people_to_add += shyness_level - people_standing_up
                assert shyness_level > people_standing_up
                people_standing_up += people_to_add + si[shyness_level]
        print("Case #{}: {}".format(i, people_to_add))
                
        




if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(sys.argv[0] + " <path_to_input_file>")
    else:
        standing_ovation(sys.argv[1])
