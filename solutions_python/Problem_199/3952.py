# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

def check(str):
	for c in str:
		if c != '+':
			return False
	return True

def flip(str,i,n):
	ans = ""
	for k in xrange(0,len(str)):
		if i <= k and k < i + n:
			if str[k] == '+':
				ans += '-'
			else:
				ans += '+'
		else:
			ans += str[k]
	return ans

def test(panc,num):
	d = {panc: 0}
	arr = [panc]
	while(len(arr) > 0):
		p = arr.pop(0)
		count = d[p]
		if check(p):
			return count
		for x in xrange(0,len(p)-num+1):
			q = flip(p,x,num)
			if not q in d:
				d[q] = count + 1
				arr.append(q)
	return "IMPOSSIBLE"







t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
	split = raw_input().split(" ")
	panc = split[0]
	num = int(split[1])  # read a list of integers, 2 in this case
	print "Case #{}: {}".format(i, test(panc,num))
  	# print "Case #{}: {} {}".format(i, panc,num)



