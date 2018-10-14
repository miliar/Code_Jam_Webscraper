
def solve(c , f , x):

	total = 0
	satisfied  = False
	cur = 2

	while not satisfied:
		
		j = x / cur
		k = ( c / cur ) + (x / (f+ cur))
		l = c /cur
		# print "j",j ,"k" ,k ,"cur" , cur ,"total" , total

		if (k < j):
			total = total + l
			cur = cur + f


		else :
			satisfied = True
			total = total + j


	return total




# print solve(500.0 , 4.0 , 2000.0)
# print solve(30.0,1.0,2.0)
# print solve(30.0,2.0,100.0)
# print solve(30.50000,3.14159,1999.19990)
# print solve(500.0,4.0,2000.0)


fin = open(r"C:\Documents and Settings\Administrator\My Documents\Downloads\B-large.in")
fout = open(r"out\j.otr" , "w")

l = int(fin.readline().rstrip('\n'))

for x in xrange(l):
	in1 = fin.readline().rstrip('\n')
	in2 = in1.split()

	fout.writelines("case #"+ str( x + 1) + ": "+ "%.7f"%(solve(float(in2[0]) , float(in2[1]) , float(in2[2])),)+"\n")
	fout.flush()


fin.close()
fout.close()




