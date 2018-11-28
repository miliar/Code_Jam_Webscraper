f = open('c-small.txt')

pairs = {}

"""
def is_recycled(num1, num2, n, m):
	if (num1 >= n and num1 <= m
		and num2 >= n and num2 <= m
		and )
"""

def recycled(n, m):
	count = 0
	nums = []
	mlen = len(str(m))
	for i in range(n, m+1):
		s = str(i)
		#print s, m, len(s), mlen
		for u in range(1,len(s)+1):
			p = s[-u:]
			num = int(p + s[:-u])
			if (num <= m and num >= i 
					and (i, num) not in nums 
					and not i == num
					and len(str(num)) == mlen):
				#print s, num 
				count+=1
				#nums.append(num)
				nums.append((i, num))
				nums.append((num, i))

	return count




outstr = ''
outf = open('c-small.out', 'w')
num = int(f.readline())
for l in range(0,num):
	line = f.readline().strip()
	n,m = map(int, line.split())
	output = recycled(n,m)

	outstr = "Case #%d: %s\n" % (l+1, output)

	# output
	print outstr,
	outf.write(outstr)

f.close()
outf.close()
