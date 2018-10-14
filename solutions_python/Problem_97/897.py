#!python
import sys
import string

def recycle(num):
	result = []
	s_num =  str(num)
	i = 1
	while i < len(s_num):
		left = s_num[:i]
		right = s_num[i:]
		recycle_num = right + left
		if recycle_num[0] != '0' and int(recycle_num) != num:
			result.append(int(recycle_num))
		#print "result[-1]= ",result[-1]
		i += 1
	#print "In func. recycle, result=%s, set(result)=%s, list(set(result))=%s" % (result, set(result), list(set(result)))
	return list(set(result))
	
def recycled(input):
	input = input.split()
	A = int(input[0])
	B = int(input[1])
	pairs = 0
	#print "Range: ", range(A, B+1)
	for n in range(A, B+1):
		recycle_n = recycle(n)
		#print "Recycled  list", recycle_n
		for m in recycle_n:
			if n < m <= B:
				pairs += 1
	return pairs
	
def main(*args):
	if len(args) < 2:
		print "Usage:\n", args[0], " <file>\n"
		return
	file = open(args[1])
	text = file.read().split('\n')
	arr = list(text)
	#print arr
	
	cases = int(arr[0])	
	i = 1
	while i <= cases:
		print "Case #%s: %s" % (i, recycled(arr[i]))
		i += 1

if __name__ == '__main__':
	#print recycle(101)
    sys.exit(main(*sys.argv))