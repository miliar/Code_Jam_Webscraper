import math
import sys
import time

try: # Use psyco if available
	import psyco
	psyco.full()
except ImportError:
	pass

def main():
	dictionary={}
	
	myfile = open("origin")
	refer = open("permute")
	
	for line in myfile.readlines():
		p=refer.readline()
		for i in xrange(len(line)):
			dictionary[line[i]]=p[i]
	dictionary['q']='z'
	dictionary['z']='q'
	myfile.close()
	refer.close()
	
#	sorted(dictionary.items())
#	for v in sorted(dictionary.items()):#enumerate(dictionary):
#		print v
	#print dictionary

	infile = open("A-small-attempt0.in")
	output = file("output_20120414_1A.txt", 'w')
	infile.readline()
	l=0
	for line in infile.readlines():
		l+=1
		output.write('Case #')
		output.write(str(l))
		output.write(': ')
		for i in xrange(len(line)):
			output.write(dictionary[line[i]])   
	infile.close()
	output.close()

main()



