#!/usr/bin/env python3

import sys, os

with open(sys.argv[1], 'r') as input:
    with open("out_" + os.path.basename(os.path.splitext(sys.argv[0])[0]) + ".txt", 'w') as output:

        
        nbCases = int(input.readline().rstrip())
        print(str(nbCases) + " cas à traiter.")

        for case in range(0,nbCases):
            clappingPeople = 0
            friends = 0
            (Smax, people) = input.readline().rstrip().split()
            for i in range(0, len(people)):
                if(clappingPeople < i):
                    newFriends = i - clappingPeople
                    friends += newFriends
                    clappingPeople += newFriends
                clappingPeople += int(people[i])
            print("Case #" + str(case + 1) + ": " + str(friends), file=output)
        print("Fait, " + str(nbCases) + " traité(s).")
        
