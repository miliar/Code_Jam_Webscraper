

def input() :
	t = int( raw_input())
	inp = list()
	rows = list()
	for i in xrange(0,t) :
		val = raw_input()
		l = val.split()
		inp.append(l)
		val = raw_input()
		rows = val.split()
		#rows.append(l1)
		r = int(l[0])
		k = int(l[1])
		n = int(l[2])
		amount = 0
		for j in xrange(0, r) :
			flag = 0
			sum = 0
			intflag = 0
			if flag < n :
				for items in rows :
					sum += int(items)
					if sum > k :
						amount = amount + sum - int(items)
						#flag = rows.index(items)
						row1 = rows[0:flag]
						rows = rows[flag:n]
						for item in row1 :
							rows.append(item)
						intflag = 1
						break
					flag = flag + 1
				if intflag == 0 :
					for items in rows :
						amount = amount + int(items)
		print "Case #%s: %d" %(i+1, amount)	
							

#def calculate (t, inp, rows) :

if __name__ == "__main__" :
	input()
	#calculate (t, inp, rows)
