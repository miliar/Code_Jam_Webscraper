import math

filename = "A-large.in"
outf = file(filename + ".out", "w")
rows = [i.strip() for i in file(filename).readlines()]
#print rows


def get_row():
	global rows
	temp = rows[0]
	rows = rows[1::]
	return temp



num_cases = int(get_row())


def calc(lst, K):
	##print "Enter calc: " + str(lst) + ", " + str(K)
	curr_rad = 0
	result = 0
	while (K > 0):
		max_cont = 0
		node = None
		for i in lst:
			surface = max((math.pi * (i[0]*i[0])) - (math.pi * (curr_rad*curr_rad)), 0)
			circ = 2 * math.pi * i[0] *  i[1]
			area = circ + surface
			#print "surface " + str(surface)
			#print "circ " + str(circ)
			if (area >= max_cont):
				max_cont = area
				node = i
		#print K
		#print node
		#print lst
		K -= 1
		lst.remove(node)
		result += max_cont
		curr_rad = max(node[0], curr_rad)
	return result





for i in range(num_cases):
	#parse case
	#math.pi
	N, K = get_row().split(" ")
	N = int(N)
	K = int(K)

	#print "i: " + str(i) + ", N: " + str(N) + ", K: " + str(K)
	lst = []
	for j in range(N):
		rad, height = get_row().split(" ")
		rad = float(rad) * 1.0
		height = float(height) * 1.0
		lst.append((rad, height))
	


	calc_res = calc(lst, K)
	#print "Case #" + str(i+1) + (": %06f" % calc_res)
	outf.write("Case #" + str(i+1) + (": %06f" % calc_res) + "\n")

