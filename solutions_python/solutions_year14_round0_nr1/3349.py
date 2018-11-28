#! /usr/bin/python 2.7

import time
import sys

def main():
    f = open(sys.argv[1])
    lines = f.readlines()
    T = int(lines[0])
    counter = 1
    for case in range(T):
		checkTrick(counter,lines,case+1)
		counter += 10


def checkTrick(counter,lines,case):
    row1 = int(lines[counter])
    list1 = lines[counter + row1].split()
    set1 = set(list1)
    row2 = int(lines[counter + 5])
    list2 = lines[counter + row2 + 5].split()
    set2 = set(list2)
    result = set1.intersection(set2)
    resultLength = len(result)
    if resultLength == 1:
        print "Case #"+ str(case) +":",list(result)[0]
    elif resultLength == 0:
        print "Case #"+ str(case) +":","Volunteer cheated!"
    else:
        print "Case #"+ str(case) +":","Bad magician!"

if __name__ == '__main__':
#	startTime = time.clock()
	main()
#	sys.stderr.write("Completed in {} seconds.\n".format(time.clock() - startTime))
