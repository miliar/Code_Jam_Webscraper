







def input() :
	t = int( raw_input())
	for i in xrange(0,t) :
		flag = 0
		val = raw_input()
		inp = val.split()
		n = int(inp[0])
		l = list()
		for j in xrange(0,n) :
			   	l.append(0)
		k = int(inp[1])
		if k % 2 == 0 :
			   print "Case #%d: OFF" % (i+1)
		else :
			for j in xrange(0, k) :
				   for iter in xrange(0,n) :
				   		if iter == 0 :
				   			l[iter] = l[iter] ^ 1
				   		elif l[iter-1] == 0 :
				   			l[iter] = l[iter] ^ 1
				   		else :
							break
					  
			for items in l :
				if items != 1 :
						print "Case #%d: OFF" % (i+1)
						flag = 1
						break

			if flag == 0 :
				print "Case #%d: ON" % (i+1)
				#break

				


if __name__ == "__main__" :
        input()

