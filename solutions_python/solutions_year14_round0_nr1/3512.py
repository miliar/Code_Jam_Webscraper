import math
import copy
import logging
import string
import sys

trace = logging.info



def main(arg_file):
    input = open(arg_file)
    nTestCases = int(input.readline())
    for testCase in range(0, nTestCases):
        row1 = int(input.readline()) - 1
        m1 = []
        for i in range(1, 5):
        	m1.append([int(x) for x in input.readline().split(" ")]);
        row2 = int(input.readline()) - 1
        m2 = []
        for i in range(1, 5):
        	m2.append([int(x) for x in input.readline().split(" ")]);
       	
       	# recorre la fila elegida en m1
       	cont = 0
       	num = 0
       	output = ""
       	for i in range(0, 4):
       		trace("Compare %i in %s"%(m1[row1][i], m2[row2]));
       		if m1[row1][i] in m2[row2]:
       			cont = cont + 1
       			num = m1[row1][i]
       	if cont == 1:
       		output = num
       	elif cont == 0:
       		output = "Volunteer cheated!"
       	else:
       		output = "Bad magician!"
        print "Case #%i: %s" % (testCase + 1, output)
    input.close()


if __name__ == "__main__":
    logging.getLogger().setLevel(logging.CRITICAL)
    # descomentar para ver llamadas a trace()
    #logging.getLogger().setLevel(logging.INFO)
    main(sys.argv[1])
