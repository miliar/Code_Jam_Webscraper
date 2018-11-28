#!/usr/bin/python
import sys

def get_dig(n):
	for i in range(1, 24):
		if n<2**i:
			return i
	return 24

def patrick_sum(n0, n1):
	
	if n0>n1:
		m = get_dig(n0)
	else:
		m = get_dig(n1)
	
	s = n0+n1
	for i in range(0, m+1):
		if (n0&(2**i))>>i == 1 and (n1&(2**i))>>i == 1:
			s -= 2**(i+1)

	return s



if len(sys.argv) == 3:
	lines = open(sys.argv[1], 'r').readlines()
	fw = open(sys.argv[2], 'w')
else:
	sys.exit('Usage: %s in_filename out_filename' % sys.argv[0])


"""
lines = ['3'
,'5'
,'1 2 3 4 5'
,'3'
,'3 5 6'
,'4'
,'2 3 5 8']
"""

"""
for i in range(0, 3+1):
	for j in range(0, 5+1):
		for k in range(0, 6+1):
			psum0 = patrick_sum(i, j)
			psum0 = patrick_sum(psum0, k)
			psum1 = patrick_sum(3-i, 5-j)
			psum1 = patrick_sum(psum1, 6-k)
			print i,j,k,'-', psum0, psum1, '-', i+j+k, 14-(i+j+k)
"""



#print patrick_sum(5,4)
#print patrick_sum(7,9)
#print patrick_sum(50,10)


numofcases = int(lines[0])
cursor = 1
for i in range(0, numofcases):
	
	numofpieces = int(lines[cursor])
	cursor += 1
	param = lines[cursor].split(' ')
	cursor += 1
	
	pieces = []
	for j in range(0, numofpieces):
		pieces.append(int(param[j]))
	
	max_d = get_dig(max(pieces))
	pind = []
	for j in range(0, max_d):
		pind.append(0)
	
	for j in range(0, numofpieces):
		di = get_dig(pieces[j])
		for k in range(0, di):
			if pieces[j]&(2**k)>0:
				pind[k] += 1
	#print pind
	
	result = ''
	for j in pind:
		if j%2==1:
			result = 'NO'
			break
	
	if result != 'NO':
		
		sean_sum = 0
		for j in range(0, numofpieces):
			sean_sum += pieces[j]
		
		pieces.sort()
		
		
		sub_d = 0
		"""
		for j in pieces:
			d = get_dig(j)
			
			f = True
			for k in range(1, d):
				if pind[k]==0:
					pass
				elif ((j & (2**k))>>k) == 1 and pind[k]%2==0:
					pass
				else:
					f = False
			
			if f:
				sub_d = j
				break
		"""
		sub_d = pieces[0]
		
		
		#print pind
		
		#print sean_sum-sub_d, sub_d
		if sean_sum-sub_d < sub_d:
			print 'omg'
		result =  str(sean_sum - sub_d)
	
	print 'Case #' + str(i+1) + ': ' + result
	fw.write('Case #' + str(i+1) + ': ' + result + '\n')

fw.close()

