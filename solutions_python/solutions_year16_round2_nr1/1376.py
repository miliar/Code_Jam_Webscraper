def getdigits(instr):
	a = list(instr.lower())
	digit = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
	digits = [list(i) for i in digit]
	b = []
	
	while 'z' in a:
		for i in digits[0]:
			a.remove(i)
		b.append(0)
	while 'w' in a:
		for i in digits[2]:
			a.remove(i)
		b.append(2)
	while 'u' in a:
		for i in digits[4]:
			a.remove(i)
		b.append(4)
	while 'x' in a:
		for i in digits[6]:
				a.remove(i)
		b.append(6)
	while 's' in a:
		for i in digits[7]:
				a.remove(i)
		b.append(7)	
	while 'f' in a:
		for i in digits[5]:
				a.remove(i)
		b.append(5)
	while 'r' in a:
		for i in digits[3]:
			a.remove(i)
		b.append(3)	
	while 'o' in a:
		for i in digits[1]:
			a.remove(i)
		b.append(1)	
	while 'g' in a:
		for i in digits[8]:
				a.remove(i)
		b.append(8)
	while 'i' in a:
		for i in digits[9]:
				a.remove(i)
		b.append(9)
	
	b.sort()
	
	return ''.join(str(i) for i in b)
def main():
	filename = 'A-large.in'
	output = 'A-large.out'
	f = open(filename,'r')
	#Output file
	out = open(output,'w')
	while True:
		line = f.readline()
		if line == '':
			break
		num_tests = int(line)
		for i in xrange(num_tests):
			line = f.readline()
			num = getdigits(line)
			s = 'Case #%s: ' %(i+1)
			s = s + str(num)
			out.write(s)
			out.write('\n')
		
if __name__ == "__main__":
	main()