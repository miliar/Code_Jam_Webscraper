def is_palindrome(i):
	si = str(i)
	for i in xrange(len(si)/2):
		if si[i] != si[len(si)-i-1]:
			return False
	return True

def count_palindrome(f,t):
	count = 0
	maxroot = int(t ** 0.5) + 1
	minroot = int(f ** 0.5)
	for i in xrange(1,maxroot+1):
		count += 1 if is_palindrome(i) and is_palindrome(i ** 2) and f <= i ** 2 <= t else 0
	return count

if __name__ == "__main__":
	for tcase in xrange(1,int(raw_input())+1):
		f,t = [int(c) for c in raw_input().split()]
		print "Case #%d: %d" %(tcase,count_palindrome(f,t))