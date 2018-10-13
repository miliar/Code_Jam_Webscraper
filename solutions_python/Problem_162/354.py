import math

def flip_digs(g):
	res = 0
	while g > 0:
		res = res*10 + g % 10
		g /= 10
	return res

def rec_solve(val):	
	if val == 1:
		return 1
	if flip_digs(val) >= val or val % 10 == 0:
		return 1 + rec_solve(val - 1)
	return 1 + min(rec_solve(val - 1), rec_solve(flip_digs(val)))
	
def fill_table(max_v):
	tbl = [-1] * 25 * max_v
	for j in range(25):
		tbl[j*max_v] = 1
	for j in range(max_v):
		tbl[j] = j + 1
	for j in range(24):
		for k in range(max_v - 1):
			if (k+2)%10 != 0:
				tbl[(j+1)*max_v + (k+1)] = 1 + min(tbl[j*max_v + flip_digs(k+2) - 1], tbl[(j+1)*max_v + k])
			else:
				tbl[(j+1)*max_v + (k+1)] = 1 + tbl[(j+1)*max_v + k]
	return tbl

#PATH = "C:/In/2015Round1B/Q1/test.txt"
PATH = "C:/In/2015Round1B/Q1/A-small-attempt0.in"
f_in = open(PATH,'r')
f_out = open(PATH + ".out",'w')
nlines = int(f_in.readline())
result = ''
max_v = 10**6
tbl = fill_table(max_v)
for k in range(nlines):
	val = int(f_in.readline())
	result =tbl[(val - 1) + max_v*24]
	#result = rec_solve(10**6)
	print "Case #" + str(k + 1) + ": " + str(result) + "\n"
	f_out.write("Case #" + str(k + 1) + ": " + str(result) + "\n")
f_in.close()
f_out.close()