dp = [1234567654321, 1000002000001, 1020304030201, 40000800004, 1232346432321, 121242121,
	100000020000001, 1004006004001, 4000008000004, 44944, 1002001, 9, 1024348434201, 12102420121,
	4004009004004, 100020001, 404090404, 12345654321, 1234321, 14641, 10201, 1, 121, 1214428244121,
	1210024200121, 10000200001, 4008004, 12321, 1022325232201, 125686521, 40804, 123454321, 400080004,
	484, 1002003002001, 1212225222121, 104060401, 10221412201, 102030201, 4]

def precompute():
	for i in xrange(1,10**7+10):
		if palindrome(i) and palindrome(i**2):
			dp.add(i**2)

def palindrome(number):
	string = str(number)
	length = len(string) - 1
	for i in xrange(length):
		if string[i] != string[length - i]:
			return False
	return True


def solve(li):
	for num in xrange(len(dp)):
		if dp[num] < li[0]:
			pass
		else:
			for hi in xrange(num,len(dp)):
				if dp[hi] > li[1]:
					return len(dp[num:hi])


def main():
  #precompute()
	dp.sort()
	tests = input()

	for test_case in xrange(1, tests+1):
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
