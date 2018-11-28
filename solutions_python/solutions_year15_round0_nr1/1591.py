#!/usr/bin/python

import sys

def parse_input(file_):
    with open(file_, 'r') as f:
        N = int(f.readline())
        with open(file_.replace("in", "out"), "a") as outfile:
            outfile.truncate(0)
        for case in range(1, N+1):
            line = f.readline()[:-1]
            S = int(line.split(" ")[0])
            counts = line.split(" ")[1]
            friends = 0
            people = 0
            for i in range(0, len(counts)):
                if people < i:
                    friends = friends + (i - people)
                    people = i
                people = people + int(counts[i])

            with open(file_.replace("in", "out"), "a") as outfile:
                outfile.write("Case #" + str(case) + ": " + str(friends) + "\n")

parse_input(sys.argv[1])
