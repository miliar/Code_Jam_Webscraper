
file = "./B-large.in"
file_ans = "./tidy.out"


def is_tidy(n):
	last = n % 10
	while n>0:
		dig = n % 10
		if dig>last:
			return False
		n /= 10
		last = dig
	return True

def find_last(n):
	last_good = 0
	for i in range(n+1):
		if is_tidy(i):
			last_good = i
	#print "last good:", n, last_good
	return last_good

def find_last_quick(n):
	if n<10:
		return n

	s = list(str(n))
	n = len(s)
	for i in range(1, n):
		if s[i]<s[i-1]:

			# fill with 9s to the right
			for j in range(i, n):
				s[j] = '9'

			j = i-1
			#print "j=", j

			
			while j>0 and s[j]==s[j-1]:
				s[j] = '9'
				j -= 1

			#print "j=", j

			if j<0:
				s = s[1:]
			else:
				s[j] = chr(ord(s[j])-1)
			break
	
	return int(''.join(s))



#for i in range(200):
#	print i, find_last_quick(i)



# for i in range(0, 999):
# 	a = find_last(i)
# 	b = find_last_quick(i)
# 	if a != b:
# 		print i, a, b

#print is_tidy(191)



with open(file, "r") as f:
	with open(file_ans, "w") as fout:

		T = int(f.readline())
		for t in range(T):
			n = int(f.readline())

			sol = find_last_quick(n)
			fout.write("Case #%d: %s\n" % (t+1, sol))
				


