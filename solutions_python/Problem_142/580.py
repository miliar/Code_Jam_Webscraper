def substring(a,b):
	if len(a) > len(b):
		return a[:len(b)] == b
	if len(b) > len(a):
		return b[:len(a)] == a

	return a == b;

T = int(raw_input())

for _t in range(1,T+1):
	#print _t
	N = int(raw_input())

	a = raw_input()
	b = raw_input()

	answer = 0
	possible = True

	last_a,last_b = "",""
	
	while not substring(a,b) and possible and a != b and a != last_a and b!= last_b:
		i = 0
		last_a,last_b = a,b
		while possible and i < min(len(a),len(b)):
			#print a[i] ,b[i]
			if possible and a[i] != b[i]:
				if i != 0:
					if a[i-1] == a[i]:
						a = a[:i] + a[i+1:]
						answer += 1
						i -= 1
						#print "---a"
					elif b[i-1] == b[i]:
						b = b[:i] + b[i+1:]
						answer += 1
						i -= 1
						#print "---b"	
					else:
						#print "no posible"
						possible = False
				else:
					#print "firs"
					possible = False

			i += 1
			"""
			print a == last_b , b == last_b
			print possible
			print last_a
			print a
			print last_b
			print b
			raw_input()
			"""
	
	if possible and len(a) != len(b):
		possible = substring(a,b)

		answer += abs(len(a) - len(b))

		last = a[min(len(a),len(b))-1]

		end = a[- (len(a) - len(b)) :] if len(a) > len(b) else b[- (len(b) - len(a)) :]
		
		for x in end:
			possible = possible and (x == last)

	print "Case #{0}: {1}".format(_t, answer if possible else "Fegla Won")