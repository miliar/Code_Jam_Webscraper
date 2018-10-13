#!/usr/bin/python

def main():
	
	# Open a file
	fo = open("A-small-attempt0.in", "r")
	out = open("A-small-attempt0.out", "w")


	ncase = int(fo.readline())
	#print ncase
	#print str
	#for i in range(0, ncase):

	#lines = fo.readlines()
	case = 0
	#print len(lines)
	
	for line in fo:
	 	#print line
	 	case = case + 1
	 	cp = 0
		cf = 0
	 	vline = line.split(" ")
	 	lenk = int(vline[0])
	 	#print lenk
	 	#print "\n"
	 	if (lenk == 0):
	 		#print "if len 0"
	 		print "Case #" + str(case) + ": 0" + "\n"
	 		out.write("Case #" + str(case) + ": 0" + "\n")
	 		continue

	 	v = list(vline[1])
	 	del v[-1]
	 	print v
	 	#print len(v)
	 	i = 0
	 	#for i in range(len(v)-1):
	 	for v_i in v:
	 		#print i
	 		#v_i = int(v[i])
	 		#v_i = int(v_i)
	 		tmp = int(v_i)
	 		print "v_i " + str(v_i)
	 		print "i " + str(i)
	 		if (tmp > 0):
	 			if (cp >= i ):
	 				cp = cp + tmp
	 				print "cp=" + str(cp)
	 			else:
	 				cf = cf + i - cp
	 				#cf = cf + i
	 				print "cf=" + str(cf)
	 				cp = cp + cf + tmp
	 				#cp = cp + cf
	 				print "cp=" + str(cp)
	 		i = i + 1
	 	print "Case #" + str(case) + ": " + str(cf) +  "\n"
	 	out.write("Case #" + str(case) + ": " + str(cf) +  "\n")





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
