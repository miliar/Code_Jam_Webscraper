def nextbig(num):		
	num=list(num)
	for i in reversed(range(1, len(num))):
		if int(num[i]) < int(num[i-1]):
			num[i]='9';num[i-1]=str(int(num[i-1])-1)	
			for j in range(i, len(num)):
				num[j]='9'		
	return ''.join(num).lstrip('0')			
if __name__ == '__main__':
	f = open('out.out', 'w')
	with open('B-large.in', 'r') as fle:
		r = fle.readlines()
		t = int(r[0][:-1])
		for i in range(1, t+1):
			n = r[i][:-1]								
			f.write('Case #' + str(i) + ': '+ nextbig(n) + '\n')						
		f.close()	 
	
		