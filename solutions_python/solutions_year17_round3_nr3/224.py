import itertools

error = 0.000001

def binom(x,y):
	if y == x:
	    return 1
	elif y == 1:         # see georg's comment
	    return x
	elif y > x:          # will be executed only if y != 1 and y != x
	    return 0
	else:                # will be executed only if y != 1 and y != x and x <= y
	    a = math.factorial(x)
	    b = math.factorial(y)
	    c = math.factorial(x-y)  # that appears to be useful to get the correct result
	    div = a // (b * c)
	    return div  

fd = open("in3.in", "r")

lines = fd.readlines()

testcases = int(lines[0])

fout = open("out3", "w")

line_ind = 1
case = 1
while line_ind < len(lines):
	line  = lines[line_ind]
	fout.write("Case #" + str(case) + ": ")
	words = line.split()
	n = int(words[0])
	k = int(words[1])

	u = float(lines[line_ind+1])
	probs = map(float, lines[line_ind+2].split())
	

	print n, k, u, probs

	maxy = max(probs)
	# print maxy
	remaining = map(lambda x: maxy - x, probs)
	# print remaining

	sum_remaining = sum(remaining)
	if(u < sum_remaining):
		
		sorted_p = sorted(probs)

		print 2, sorted_p

		while u > 0:
			mini = sorted_p[0]
			index = 0
			what_to_reach = -1
			for i in xrange(n):
				if(sorted_p[i] > mini + error):
					index = i
					what_to_reach = sorted_p[i]
					break
			# print index
			what_to_add = min([what_to_reach - mini, u])/float(index)
			added = map(lambda x: what_to_add + x, sorted_p[:index])
			
			sorted_p = added + sorted_p[index:]
			u -=  what_to_add * index
			# print u, what_to_add, what_to_reach, mini
		probs = sorted_p[:]
	else:
		remaining_ratio = map(lambda x: x, remaining)
		# print "Rem: ", remaining_ratio
		probs = [ a+b for (a,b) in zip(probs,remaining_ratio) ] 
		# print 2, probs
		u -= sum_remaining

		probs = map(lambda x: x + (u/n), probs)
	
	# print 3, probs


	mul = 1
	for i in probs:
		mul *= i


	print "Result: ", mul
	fout.write(str(mul) + "\n")

	line_ind += 3
	case += 1