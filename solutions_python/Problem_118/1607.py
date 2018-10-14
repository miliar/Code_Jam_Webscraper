# def A050250(n):
# 	if n % 2 == 0:
# 		return 2 * (10 ** (n/2) - 1)
# 	else:
# 		return 11 * 10 ** ((n-1)/2) - 2

# def get_palidromes(high):
# 	if high < 10:
# 		return high
# 	elif high == 10:
# 		return 9
# 	exp = len(str(high)) - 1
# 	i = []
# 	for j in range(exp, exp%2==0, -2):
# 		o = 10 ** (j+1) + 1
# 		if j == exp:
# 			d = high
# 		else:
# 			d = temp
# 		i.append(d / o)
# 
# def old_get_palindromes(low, high):
# 	if high < 2:
# 		return 0
# 	d = []
# 	m, n = 0, high - 1
# 	while n > 0:
# 		d.append(n % 10) 
# 		n /= 10
# 		m += 1
# 	n = m - 1
# 	result = A050250(n)
# 	
# 	m, i, j = n, 0, n / 2
# 	d[n] -= 1
# 	while m - i >= 2:
# 		result += d[m] * (10**j)
# 		m -= 1
# 		i += 1
# 		j -= 1
# 	result += d[m]
# 	if d[i] >= d[m]:
# 		result += 1
# 	return result
	
def generate_palindromes(limit):
	results = set([i for i in [1, 4, 9] if i < limit])
	cont, i = True, 1
	while cont:
		opp = str(i)[::-1]
		if sorted(set(opp+"012")) == list("012"):
			cont = False
			for d in list("012")+[""]:#([""] if len(opp)%3==0 else []):
				n = int("%d%s%s"%(i, d, opp))
				if n**2 <= limit:
					cont = True
					if str(n**2) == str(n**2)[::-1]:
					# if int(n**0.5) == n**0.5 and str(int(n**0.5)) == str(int(n**0.5))[::-1]:
						results.add(n**2)
		i += 1
	return results
	
def count_fair_square(low, high):
	left = 0
	while left+1<len(fair_squares) and fair_squares[left + 1] < low:
		left += 1
	if low != fair_squares[left]: left += 1
	
	count = 0
	for i in range(left, len(fair_squares)):
		if fair_squares[i] > high:
			break
		count += 1
	# print left
	return count
		
	
if __name__=='__main__':
	import argparse
	parser = argparse.ArgumentParser(description='Counts fair and square numbers between given boundaries')
	parser.add_argument('--verbose', '-v', action='store_true')
	parser.add_argument('infile', type=str, help='in file')
	parser.add_argument('outfile', type=str, nargs="?", help='out file (defaults to infile with extension changed to .out)')
	args = parser.parse_args()

	infile = open(args.infile, "r")
	outfile = open(args.outfile if args.outfile is not None else args.infile.rsplit(".")[0]+".out", "w")
	tests = int(infile.readline())
	fair_squares = sorted([1, 4, 9, 1004006004001, 1020304030201, 44944, 1002001, 12102420121, 1002003002001, 400080004, 4004009004004, 100020001, 404090404, 12345654321, 40000800004, 123454321, 14641, 1210024200121, 121242121, 1214428244121, 40804, 1232346432321, 10000200001, 4008004, 12321, 1000002000001, 1022325232201, 125686521, 121, 10201, 4000008000004, 484, 1234321, 10221412201, 1024348434201, 1234567654321, 104060401, 1212225222121, 102030201])
	for i in range(tests):
		low, high = [int(j) for j in infile.readline().split(" ")]
		s = "Case #%d: %d"%(i+1, count_fair_square(low, high))
		if args.verbose:
			print s
		outfile.write(s + ("\n" if i < tests-1 else ""))
	infile.close()
	outfile.close()