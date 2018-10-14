def test_func(max_shyness, nums):
	people = 0
	to_add = 0
	for i in xrange(0, max_shyness + 1):
		if people < i:
			to_add += i - people
			people += i - people
		people += int(nums[i])
	return to_add

def main():
	test_num = int(raw_input())
	for test in xrange(test_num):
		test_string = raw_input().split()
		print 'Case #%d: %d' % (test + 1, test_func(int(test_string[0]), test_string[1]))

if __name__ == '__main__':
	main()