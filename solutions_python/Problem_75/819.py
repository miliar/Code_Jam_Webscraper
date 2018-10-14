#!/usr/bin/env python

def magic(comb, oppo, seq):
	lst = []
	for w in seq:
		#print "w:", w
		if lst == []:
			lst.append(w)
		else:
			last = lst[-1]
		#	print 'last:', last
			if w+last in comb:
				lst[-1] = comb[w+last]
			else:
				for j in lst:
					if oppo.count(j+w) > 0:
						lst = []
						break
				if lst != []:
					lst.append(w)
	return lst

def process(data):
	c = int(data[0])
	d = int(data[c+1])
	n = int(data[c+d+2])
	comb = {} 
	for i in range(c):
		w = data[i+1]
		comb[w[0]+w[1]] = w[2]
		comb[w[1]+w[0]] = w[2]
	oppo = []
	for i in range(d):
		oppo.append(data[c+2+i])
		oppo.append(data[c+2+i][::-1])
	seq = data[c+d+3]
#	print "%s %s %s" %(comb, oppo, seq)
	return (comb, oppo, seq)

if __name__ == '__main__':
	f = open('B-large.in')
	data = f.readline().split()
	T = int(data[0])
	for i in range(T):
		data = f.readline().split()
		(comb, oppo, seq) = process(data)	
		lst = magic(comb, oppo, seq)
		outstr =  "Case #%s: [" %(i+1)
		for w in lst:
			 outstr = outstr + w + ", "
		if lst == []:
			outstr = outstr + "]"
		else:
			outstr = outstr[:-2] + "]"
		print outstr
