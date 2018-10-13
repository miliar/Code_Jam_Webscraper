#!/usr/bin/python

def main():
	
	# Open a file
	fo = open("D-small-attempt0.in", "r")
	out = open("D-small-attempt0.out", "w")


	ncase = int(fo.readline())
	print ncase
	#print str
	#for i in range(0, ncase):

	#lines = fo.readlines()
	case = 0
	#print len(lines)
	
	for line in fo:
	 	#print line
	 	case = case + 1
	 	
	 	vline = list(line.split())
	 	#print vline
	 	x = int(vline[0])
	 	r = int(vline[1])
	 	c = int(vline[2])
	 	if ( (x<7) and (((r * c) % x) == 0) and max(r, c) >= x and min(r,c) >= x-1 ): 
	 		print "Case #" + str(case) + ": GABRIEL"  +  "\n"
	 		out.write("Case #" + str(case) + ": GABRIEL"  +  "\n")
	 	else:
	 		print "Case #" + str(case) + ": RICHARD"  +  "\n"
	 		out.write("Case #" + str(case) + ": RICHARD"  +  "\n")






	#str = fo.read(10);
	#print "Read String is : ", str

	# Check current position
	#position = fo.tell();
	#print "Current file position : ", position

	# Reposition pointer at the beginning once again
	#position = fo.seek(0, 0);
	#str = fo.read(10);
	#print "Again read String is : ", str

	#WRITE FILE
	#fo.write( "Python is a great language.\nYeah its great!!\n");

	# Close opend file
	fo.close()
	out.close()

	# out = open("Prova.out", "r+")
	# lines = out.readlines()
	# #lines = lines[:-1]
	# print lines


if __name__ == "__main__":
	main()
