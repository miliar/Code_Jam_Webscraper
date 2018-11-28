import math

#	Get the input
w = open("fns.out", "w")
f = open("C-small-attempt0.in", "r")
f = f.readlines()
cases = int(f[0].strip('\n'))
case = 1


#	Functiont hat determines whether a number is a palindrome
def isPalindrome(number):

	reverse = 0
	n = number
	while n > 0:

		reverse = reverse * 10 + n % 10
		n /= 10

	#	If it is a palindrome, this should be true
	return number == reverse


#	Get minimum and maximum
for case in range(1, len(f)):
	items = f[case].strip('\n').split(' ')
	mi = int(items[0])
	ma = int(items[1])

	fairsquares = 0

	#	Loop up to maximum
	for p in range(mi, ma+1):

		if isPalindrome(p):

			#	Now get the square root
			sq = int(math.sqrt(p))
			if sq ** 2 == p:

				#	Check the square root is a palindrome
				if isPalindrome(sq):
					fairsquares += 1


	w.write("Case #%s: %s\n" % (case, fairsquares))



