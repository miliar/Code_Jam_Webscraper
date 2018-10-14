dp = {1234567654321, 1, 1020304030201, 400080004, 1000002000001, 9, 1004006004001, 4000008000004, 
	44944, 1234321, 121, 10201, 1002003002001, 4, 4004009004004, 12321, 404090404, 12345654321,
	40000800004, 123454321, 12102420121, 14641, 121242121, 1214428244121, 1210024200121, 1232346432321, 
	10000200001, 4008004, 100020001, 1022325232201, 102030201, 40804, 484, 1002001, 10221412201, 
	1024348434201, 104060401, 1212225222121, 125686521}

'''
def precompute():
	for i in xrange(1,10**7):
		if palindrome(i) and palindrome(i**2):
			dp.add(i**2)
	print dp
'''

def palindrome(number):
	string = str(number)
	length = len(string) - 1
	for i in xrange(length):
		if string[i] != string[length - i]:
			return False
	return True


def solve(li):
	count = 0
	for num in range(li[0], li[1]+1):
		if num in dp:
			count += 1
	return count


def main():
	#precompute()
	tests = input()

	for test_case in range(1, tests+1):
		li = [int(x) for x in raw_input().split()]
		lis = []
		if li[0] > li[1]:
			lis.append(li[1])
			lis.append(li[0])
		else:
			lis = li

		print "Case #%d: %d" % (test_case, solve(lis))

if __name__ == '__main__':
	main()