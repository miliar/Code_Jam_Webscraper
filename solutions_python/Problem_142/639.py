#!/usr/bin/python
import string
import sys

def computeDist(in1, in2):
	arr = [ [9999999]*(len(in1) + 1) for x in xrange(len(in2) + 1)]
	arr[0][0] = 0 # distance between two empty strings

	for i in xrange(len(in1)):
		for j in xrange(len(in2)):
			if in1[i] == in2[j]:
				arr[j+1][i+1] = min(min(
					arr[j][i],
					1 + arr[j][i+1]),
					1 + arr[j+1][i]
					)

	res = arr[len(in2)][len(in1)]
	return res

def main():
    infile = open(sys.argv[1], "r")

    for case in range(1, int(infile.readline())+1):
        numstrings = int(infile.readline())

        strings = [infile.readline() for i in range(numstrings)]

        distances = [ [0]*numstrings for i in range(numstrings)]

        for s1ix in range(numstrings):
        	for s2ix in range(numstrings):
        		s1 = strings[s1ix]
        		s2 = strings[s2ix]
        		distances[s1ix][s2ix] = computeDist(s1, s2)
        		distances[s2ix][s1ix] = distances[s1ix][s2ix]

        mini = -1
        for row in distances:
        	rowsum = sum(row)
        	if mini == -1 or rowsum < mini:
        		mini = rowsum

        if mini == 9999999:
        	mini = "Fegla Won"

        print("Case #{0}: {1}".format(case, mini))

if __name__ == "__main__":
        main()