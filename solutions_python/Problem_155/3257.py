import math

import sys


def read_file(filename):
    """ 
    Read the text file with the given filename;
    return a list of the lines of text in the file.
    """
    try:
        f = open(filename, 'r')
        return f.readlines()
    except IOError:
        print "Error opening or reading input file: ",filename
        sys.exit()

def split_and_solve_line_list(L):
    
    numcases = L[0]
    for index, case in enumerate(L[1:]):
    	(maxShyness, crowd) = case.split(" ")   
        solve_case(index, maxShyness, crowd)
#0600061

def solve_case(casenum, maxShyness, crowd):
	totalShyness = 0
	crowdAdded = 0
	crowdString = str(crowd)
	for shyness, numWithShynessStr in enumerate(crowdString):
		if numWithShynessStr == "\n":
			with open('problem1_large.out', 'a') as outfile: outfile.write("Case #" + str(casenum + 1) + ": " + str(crowdAdded) + "\n")
			return
		numWithShyness = int(numWithShynessStr)
		if numWithShyness == 0:
			continue
		elif shyness <= totalShyness:
			totalShyness += numWithShyness
		else:
			while totalShyness < shyness:
				crowdAdded += 1
				totalShyness += 1
			totalShyness += numWithShyness
		
	

def main():
    if len(sys.argv) != 2:
        print "Usage: docdist1.py filename_1"
    else:
        filename_1 = sys.argv[1]
        lines = read_file(filename_1)
        split_and_solve_line_list(lines)

if __name__ == "__main__":
	main()
