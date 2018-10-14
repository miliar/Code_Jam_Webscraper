
def war(n , k):
	k1 = [float(c) for c in k.split()]
	n1 = [float(c) for c in n.split()]

	n1.sort()
	k1.sort()

	n1.reverse()
	k1.reverse()

	# print "n", n1 
	# print "k",k1

	k = k1[:]
	n = n1[:]
	c = 0
	for x in n:
		if(x > k[0]):
			c += 1
			k.pop()
		else:
			k.pop(0)
	# print c

	k = k1[:]
	n = n1[:]
	d = 0

	v=0 
	for h in xrange(len(n)):
		if (n[h] - k[h] ) > 0 :
			v += 1
	# print v
	for x in k:
		if x < n[0]:
			n.pop(0)
			d += 1
		elif(x > n[-1]):
			# print x , n
			n.pop()
		# elif x < n[-1]:
		# 	n.pop()
		# 	d += 1
		else:
			d += 1
			n.pop(0)
	# if (d > v):
	return str(d) + " " + str(c)
	# else:
	# 	return str(v) + " " + str(c)
	# print d


# print war("0.5","0.6")
# print war("0.7 0.2","0.8 0.3")
# print war("0.5 0.1 0.9","0.6 0.4 0.3")
# print war("0.186 0.389 0.907 0.832 0.959 0.557 0.300 0.992 0.899","0.916 0.728 0.271 0.520 0.700 0.521 0.215 0.341 0.458")


fin = open(r"C:\Users\Aymen\Downloads\D-large.in")
fout = open(r"out\test_lastb.out" , "w")

l = int(fin.readline().rstrip('\n'))

for x in xrange(l):
	fin.readline()

	fout.writelines("case #"+ str( x + 1) + ": "+ war(fin.readline().rstrip('\n') , fin.readline().rstrip('\n'))+"\n")
	fout.flush()


fin.close()
fout.close()

