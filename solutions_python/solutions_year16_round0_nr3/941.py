import sys

def divisor(n):
    '''
    n must be a positive, odd number.
    Returns None if integer n is a prime or one non trivial divisor else
    '''
    if n == 1:
        return None
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return x
    return None

primesunder100 = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def quick_divisor(n):
    '''
    n must be a positive, odd number.
    Returns None if integer n is a prime or one non trivial divisor else
    '''
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in primesunder100:
        if n % x == 0:
            return x
    return None



for testCase in range(int(input())):
	N, J = input().split(' ')
	N, J = int(N), int(J)

	print("Case #{}:".format(testCase+1))

	coinjamFound = 0

	for count in range(2**(N-2)):
		binaryString = '1'+ format(count, '0{}b'.format(N-2)) + '1'
		isCoinjam = True
		divisors = [0]*9
		for base in range(2, 11):
			nb = int(binaryString, base)
			div = quick_divisor(nb)
			if div == None:
				isCoinjam = False
				break
			else:
				divisors[base-2] = div

		if isCoinjam:
			coinjamFound += 1
			print("{} {}".format(binaryString, ' '.join(map(str, divisors))))
			print(coinjamFound, file=sys.stderr)

		if coinjamFound == J:
			break