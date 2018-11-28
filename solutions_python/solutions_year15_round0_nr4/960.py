import math
from math import *

#fname = "small"
fname = "D-small-attempt5"
#fname = "B-large"

ifile = open(fname + '.in', 'r')
ofile = open(fname + '.out', 'w+')


with ifile:
	num_case = [int(x) for x in ifile.readline().split()]

	for i in range(0, num_case[0]):
		list_int = [int(x) for x in ifile.readline().split()]
		x = list_int[0]
		r = list_int[1]
		c = list_int[2]

		if (x==1):
			print "Case #%d: GABRIEL" % (i+1)
			ofile.write("Case #%d: GABRIEL\n" % (i+1))
		elif (x==2 and (r*c)%2==0):
			print "Case #%d: GABRIEL" % (i+1)
			ofile.write("Case #%d: GABRIEL\n" % (i+1))
		elif (x==2 and (r*c)%2==1):
			print "Case #%d: RICHARD" % (i+1)
			ofile.write("Case #%d: RICHARD\n" % (i+1))
		elif (x==3):
			if ((r*c)%3!=0 or (r==1 or c==1)):
				print "Case #%d: RICHARD" % (i+1)
				ofile.write("Case #%d: RICHARD\n" % (i+1))
			else:	
				print "Case #%d: GABRIEL" % (i+1)
				ofile.write("Case #%d: GABRIEL\n" % (i+1))
		elif (x==4):
			if ((r*c)%4!=0 or (r<=2 or c<=2)):
				print "Case #%d: RICHARD" % (i+1)
				ofile.write("Case #%d: RICHARD\n" % (i+1))
			else:	
				print "Case #%d: GABRIEL" % (i+1)
				ofile.write("Case #%d: GABRIEL\n" % (i+1))
						

#		elif (x==3):
#			if ((r*c)%3!=0 or r==1 or c==1 or (r==3 and c==3)):
#				print "Case #%d: RICHARD" % (i+1)
#				ofile.write("Case #%d: RICHARD\n" % (i+1))
#			else:	
#				print "Case #%d: GABRIEL" % (i+1)
#				ofile.write("Case #%d: GABRIEL\n" % (i+1))
#		elif (x==4):
#			#if (r<4 and c<4 or r==1 or c==1)):
#			print "Case #%d: RICHARD" % (i+1)
#			ofile.write("Case #%d: RICHARD\n" % (i+1))
