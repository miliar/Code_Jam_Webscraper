import sys


# ------- Check for argument
if len( sys.argv ) < 2:
	print 'Missing input file'
	sys.exit()

def getTime(k, C, F, X):
	""" Calculates the necessary time considering that I will buy exactly k Farms"""
	T = 0.0
	x = 2.0

	# -------- for all this farms calculates necessary time for buying each of them
	for i in range(k):
		T += C / x
		x += F
	# -------- add aditional time for reaching the X number of cookies	
	T += X / x
	return T

def search(C, F, X):
	l = 0
	r = 50000

	# -------- do a ternary search to find optimal number of farms
	while r - l > 2:
		lm = (2 * l + r) / 3
		rm = (l + 2 * r) / 3

		if getTime(lm, C, F, X) < getTime(rm, C, F, X):
			r = rm
		else:
			l = lm

	# -------- select minimum from them
	sol = getTime(l, C, F, X)
	for i in range(l + 1, r + 1):
		sol = min(sol, getTime(i, C, F, X))
	return sol

# ------- processing input data

fin = open( sys.argv[1] ,'r')
data = fin.readlines()
fin.close()

# ------- writing solution

fout = open( sys.argv[1] + '_out' ,'w')

t = int( data[0] )
for i in range(1, t + 1):
	C, F, X = [float(x) for x in data[i].split(' ')]
	fout.write( 'Case #' + str(i) + ': ' + str( search(C, F, X) ) + '\n' )

fout.close()
