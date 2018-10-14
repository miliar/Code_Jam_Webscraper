#Read input file
import sys
from searchword import searchword

def main(fileName):
	setting, data = fileOpen(fileName)
	i = 1
	for d in data:
		result = searchword(d)
		print "Case #%d: %04d" % (i ,result)
		i += 1
		if i > setting:
			break

def fileOpen(fileName):
	f = open(fileName)
	i = 0
	data = []
	for line in f:
		if i == 0:
			#parse first line
			setting = int(line[:-1])
		else:
			data.append(line[:-1])
		#print line
		i += 1
	return setting,data

if __name__ == "__main__":
	if len(sys.argv) > 1:
		main(sys.argv[1])
	else:
		#import doctest
		#doctest.testmod(verbose=True)
		print "usage: exefile inputfile"
