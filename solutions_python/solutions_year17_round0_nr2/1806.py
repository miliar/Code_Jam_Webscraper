def check(num):
	num = str(num)
	for i in range(len(num)-1):
		if int(num[i]) > int(num[i+1]):
			return False
	return True

def solve(num):
	num = str(num)
	if len(num) <= 1:
		return num
	res = []
	last = False
	for i in range(len(num)-1):
		if int(num[i]) > int(num[i+1]):
			if num[i] == '0':
				notzero = len(res)-1
				while res[notzero] == '0':
					notzero -= 1
				res[notzero] = str(int(res[notzero])-1)
				res[notzero+1:] = ['9']*len(res[notzero+1:])
				res += ['9'] * (len(num) - i - 1)
				last = True
				break
			else:
				res = res + [str(int(num[i])-1)] + ['9']*(len(num)-i-1)
				last = True
				break
		else:
			res += num[i]
			last = False
	if not last:
		res += num[-1]
	return int(''.join(res))

if __name__ == '__main__':
	tc = int(input())
	for tcidx in range(1, tc+1):
		num = solve(input().strip())
		while(not check(num)):
			#print(num)
			num = solve(num)
		print("Case #{0}: {1}".format(tcidx, num))

"""
4
132
1000
7
111111111111111110
"""