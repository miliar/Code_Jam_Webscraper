import sys

#Check to see if int m is recycled from int n
def recycled(n,m):
	a = str(n)
	b = str(m)
	checked = 0
	mod = len(a)
	
	#Quick check for non-recyclability: both numbers
	#should share the same digits
	a_set = set(a)
	b_set = set(b)
	if(a_set != b_set):
		return False
	
	a_index = 0
	b_index = 0
	
	#Scan a until start of b is found, or not found
	while(checked < mod):
		a_index = (a_index + 1) % mod
		
		#If a match with a[a_index] and the start of b
		#is found, check the other characters.  If they
		#all match, return True; else, return to the while
		#loop
		if a[a_index] == b[0]:
			b_index = 0
			success = True
			for i in xrange(1,mod):
				a_index = (a_index + 1) % mod
				b_index += 1
				if(a[a_index] != b[b_index]):
					success = False
					break
			if success:
				return True
				
		checked += 1
				
	#No matches were ever found, return False
	return False

#Create a recycled number from number by moving
#rotating the last digits of number to the front.
#The number of digits to rotate is specified by
#rotate	
def recycle(number,rotate):
	a = list(str(number))
	newa = []
	
	for i in xrange(rotate):
		digit = a.pop()
		newa.insert(0,digit)
	
	for i in a:
		newa.append(i)
		
	return int(''.join(newa))
		
	
	
	
if (len(sys.argv) > 1):
	file = open(sys.argv[1],'r')
	outfile = open("output", 'w')
	cases = file.readline()
	cases = int(cases)
	iters = 0
	
	
	while(iters < cases):
		data = file.readline()
		data = data.split(' ')
		a = int(data[0])
		b = int(data[1])
		recycle_count = 0
		all_pairs = set([])
		
		
		# for i in xrange(a,b+1):
			# for j in xrange(i+1,b+1):
				# if(recycled(i,j)):
					# print i,j
					# recycle_count += 1
					
		#Create mod recycled pairs from i; increment
		#count if the recycled numbers is greater than i
		#and less than B
		
		for i in xrange(a,b+1):
			recycled = []
			for rotate in xrange(1,len(str(i))):
				recycled.append(recycle(i,rotate))
			#Delete duplicates
			recycled = list(set(recycled))
			for number in recycled:
				if (i != number and a < number and number < b):
					# print str(i) + " < " + str(number) + " < " + str(b)
					# print (i,number)
					if (i < number):
						all_pairs.add((i,number))
					else:
						all_pairs.add((number,i))
			
		recycle_count = len(all_pairs)
				
		
		outfile.write("Case #" + str(iters+1) + ": " + str(recycle_count) + '\n')
		iters += 1
		
	file.close()
	outfile.close()