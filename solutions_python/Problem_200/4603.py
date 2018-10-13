def isTidy_sort(n):
	unsorted = list(str(n))
	sort = sorted(str(n))
	return sort == unsorted

def tst_isTidy():
	# 8, 123, 
	assert isTidy_sort(224488)
	assert isTidy_sort(555)
	assert isTidy_sort(123)
	assert isTidy_sort(8)
	#20, 321, 495 and 999990
	assert not isTidy_sort(20)
	assert not isTidy_sort(495)
	assert not isTidy_sort(321)
	assert not isTidy_sort(9999990)
	for i in range(0, 10**5):
		isTidy_sort(i)

def isTidy_fast(n):
	lst = list(str(n))
	lastnum = lst[0]
	for num in lst:
		if lastnum > num:
			return False
		lastnum = num
	return True

def test_isTidy_fast():
	# 8, 123, 
	assert isTidy_fast(224488)
	assert isTidy_fast(555)
	assert isTidy_fast(123)
	assert isTidy_fast(8)
	#20, 321, 495 and 999990
	assert not isTidy_fast(20)
	assert not isTidy_fast(495)
	assert not isTidy_fast(321)
	assert not isTidy_fast(9999990)
	for i in range(0, 10**18):
		print(i)
		isTidy_fast(i)

def solve(n):
	if isTidy_fast(n):
		return n
	number = n
	while not isTidy_fast(number):
		number -= 1

	return number

def main():
	# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
	# This is all you need for most Google Code Jam problems.
	t = int(input())  # read a line with a single integer
	for i in range(1, t + 1):
	  number = int(input())  # read a list of integers, 2 in this case
	  solution = solve(number)
	  print("Case #%d: %d" % (i, solution))

if __name__ == '__main__':
	main()