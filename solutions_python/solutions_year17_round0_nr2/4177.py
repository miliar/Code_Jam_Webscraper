import sys

f = open('in.txt')
T = f.readline()

try:
	T = int(T)
except ValueError:
	print "error, line {}: Number of Test cases is not INT value".format(sys.exc_info()[-1].tb_lineno)
	exit(0)

data = f.read().splitlines();
f.close()

# for i in xrange(T):
	# print data[i]
# print "="*30

# ====================================
def make9(n):
	return "9"*n

def dec(n):
	return str(int(n)-1)

def f(n):
	length = len(n)
	end = -1
	res = ''

	if length < 2:
		return n

	for i in xrange(length-1):
		if n[i] > n[i+1]:
			end = i
			break

		res += n[i]

	if end == -1:
		return n

	dec_number = dec(n[end])
	res += dec_number
	res += make9(length - 1 - end)

	if dec_number < n[end-1] and end > 0:
		res = f(res)

	return int(res)
# ====================================

ff = open('out.txt', 'w')
for i in xrange(T):
	s = "Case #{}: {}".format(i+1, f(data[i]))
	# print s
	ff.write(s+"\n")

ff.close()