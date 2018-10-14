def solve(seq):
	sum = 0
	count = 0
	for i in range(len(seq)):
		if(sum < i):
			count += i-sum
			sum = i
		sum += seq[i]
	return count

if __name__ == '__main__':
	x = int(raw_input())
	for i in range(x):	
		s = raw_input()
		seq = [int(y) for y in s.split()[1]]
		print "Case #"+str(i+1)+": ",solve(seq)
