import sys;
def cancombine(a,b,combinestr):
	result = '0'
	if (combinestr[0] == a and combinestr[1] == b) or (combinestr[0] == b and combinestr[1] == a):
		result = combinestr[2]

	return result
		
def canoppose(arr, elem, opposestr):
	a = arr + [elem]
	if (opposestr[0] in a) and (opposestr[1] in a):
		return 1
	else:
		return 0

def disp(arr):
	str = ''
	if len(arr) == 0:
		return str
	str = arr[0]
	arr = arr[1:]
	for i in range(len(arr)):
		str = str + ", " + arr[i]
		
	return str
		
def main():
	filename = sys.argv[1]
	f=open(filename,'r')
	outf=open("output.txt", 'w')
	numtests = int(f.readline())
	total = numtests
	while numtests > 0:
		input=str.split(f.readline())
		numtests = numtests - 1
		# combine array
		combinecnt = int(input.pop(0))
		combinearr = []
		if combinecnt > 0:
			combinearr = input[0:combinecnt]
			input = input[combinecnt:]
		# oppose array	
		opposecnt = int(input.pop(0))
		opposearr = []
		if opposecnt > 0:
			opposearr = input[0:opposecnt]
			input = input[opposecnt:]
		# invoke elements
		invokecnt = int(input.pop(0))
		invokearr = input[0]
		resultarr = []
		for i in range(invokecnt):
			invoke = invokearr[i]
			if len(resultarr) == 0:
				resultarr.append(invoke)
				#print ('Invoking ', invoke, ' arr=',resultarr)
				continue
			# Check if last 2 elements can be combined
			while 1:
				combine = '0'
				for c in combinearr:
					combine = cancombine(resultarr[-1],invoke,c)
					if  combine != '0':
						last = resultarr.pop()
						resultarr.append(combine)
						#print ('match found',resultarr)
						break
					# Check this for recursive combine
				if combine != '0' and len(resultarr) > 1:
					invoke = resultarr.pop()
				else:
					break
					
			if combine == '0':
				resultarr.append(invoke)
			else:
				continue
			# Check if any of the elements are opposed
			for opp in opposearr:
				oppose = canoppose(resultarr,invoke, opp)
				if  oppose:
					#print ('going to oppose in',resultarr)
					resultarr = []
					break
			#print ('Invoking ', invoke, ' arr=',resultarr)
		
		outf.write('Case #'+str(total-numtests)+': ['+disp(resultarr)+']\n')	
		print ('Case #',str(total-numtests),': [',disp(resultarr),']\n')
		
	f.close()
	outf.close()

main()
	
		