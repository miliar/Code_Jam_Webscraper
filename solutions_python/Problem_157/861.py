mult = {('1', '1'): "1",('1', 'i'): "i", ('1', 'j'): "j", ('1', 'k'): "k",   ('i', '1'): "i", ('i', 'i'): "-1", ('i', 'j'): "k", ('i', 'k'): "-j",   ('j', '1'): "j", ('j', 'i'): "-k", ('j', 'j'): "-1", ('j', 'k'): "i",   ('k', '1'): "k", ('k', 'i'): "j", ('k', 'j'): "-i", ('k', 'k'): "-1"}

def build_mult_dp(ijk):
	n = len(ijk)
	
	# dp[x][y] = multiplication of substring ijk[x:y]
	dp = [ [''] * n for i in range(n) ]
	
	# base case diagonal
	for i in range(n):
		dp[i][i] = ijk[i]
	
	for i in range(0, n):
		for j in range(i + 1, n):
			sign = 1
			prev = dp[i][j-1]
			if prev[0] == '-':
				sign = -1
				prev = prev[1:]
			result = mult[(prev, ijk[j])]

			if result[0] == '-':
				sign = sign * -1
				result = result[1:]
			dp[i][j] = result if sign == 1 else "-" + result
	return dp
	
def multiply(ijk):
	if len(ijk) <= 1:
		return ijk
	sign = 1
	if ijk[0] == '-':
		ijk = ijk[1:]
		sign = sign * -1
	result = ijk[0]
	for i in range(1, len(ijk)):
		result = mult[(result, ijk[i])]
		if result[0] == '-':
			sign = sign * -1
			result = result[1:]
	return result if sign == 1 else "-" + result
		
	

def solve(ijk, s):
	n = len(ijk)
	# base cases
	if len(s) == 1 or n < 3:
		return False
	#dp = build_mult_dp(ijk)
	i = ""
	k = ""

	start = 0; end = n - 1
	while start <= end:
		# try to find substring 0:start that equals to i
		while start <= end:
			i += ijk[start]
			i = multiply(i)
			if i == "i":
				break
			start += 1
			
		# try to find substring end:n-1 that equals to k
		while start <= end:
			if len(k) >0 and k[0] == "-":
				k = "-"+ijk[end] + k[1:]
			else:
				k = ijk[end] + k
			k = multiply(k)
			if k == "k":
				break
			end -= 1
			
		if start <= end:
			# if found i and k to be true the middle must be j
			#if dp[start+1][end-1] == 'j':
			if multiply(ijk[start+1:end]) == "j":
				return True
		start += 1
		end -= 1
	return False
	

if __name__ == '__main__':
	in_file = open('C-small-attempt1.in', 'r')
	#in_file = open('in.txt', 'r')
	out_file = open('out.txt', 'w')
	#print multiply("ijk")
	test_cases = int(in_file.readline())
	for test_case in range(test_cases):
		L, X = [int(x) for x in in_file.readline().strip().split()]
		s = in_file.readline().strip()
		ijk = s * X
		out_file.write("Case #%d: %s\n"%(test_case+1, "YES" if solve(ijk, s) else "NO"))
		#print("Case #%d: %s\n"%(test_case+1, "YES" if solve(ijk, s) else "NO"))
	out_file.close()
		