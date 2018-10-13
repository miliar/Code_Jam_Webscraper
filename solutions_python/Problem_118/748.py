
# floor(sqrt(x))
def isqrt(x):
    if x < 0:
        raise ValueError('square root not defined for negative numbers')
    n = int(x)
    if n == 0:
        return 0
    a, b = divmod(n.bit_length(), 2)
    x = 2**(a+b)
    while True:
        y = (x + n//x)//2
        if y >= x:
            return x
        x = y

def is_palin(str):
	l = len(str)
	for i in range(l):
		if str[i] != str[l-1-i]:
			return False
	return True

# f&s numbers in [1, N]
def solve(N):
	lim = isqrt(N)
	# sqrts in [1, lim]

	res = 0
	mlen = len(str(lim))
	for x in range(mlen):
		le = x+1
		res += recgen(lim, 0, '', 1, le, 0)
	return res

def recgen(lim, cur, curstr, pow10, length, ind):
	if ind * 2 >= length:
		s2 = curstr
		s1 = s2[::-1]
		if ind * 2 > length:
			s2 = s2[1:]
		s = s1 + s2
		num = int(s)
		if num > lim:
			return 0
		if not is_palin(str(num * num)):
			return 0
		#print("Adding: ", num, cur, ind, length)
		return 1

	res = 0
	npow10 = pow10 * 10
	for dig in range(10):
		if ind == 0 and dig == 0:
			continue
		ncurstr = str(dig) + curstr
		ncur = cur + dig * pow10
		lowstr = str((ncur * ncur) % npow10)

		# Pruning!
		high = int(ncurstr[::-1])
		higha = str(high * high)
		highb = str((high + 1) * (high + 1))
		if len(higha) == len(highb):
			invalid = False
			for i in range(min(len(higha), len(lowstr))):
				if higha[i] != highb[i]:
					break
				if higha[i] != lowstr[-1 - i]:
					invalid = True
					break
			if invalid:
				continue

		res += recgen(lim, ncur, ncurstr, npow10, length, ind+1)

	return res


def main():
	#while True:
		#n = int(input())
		#print(solve(n))
	# print(solve(5000000))
	# for i in range(100000):
		# if solve(i)+1 == solve(i+1):
			# print(str(i+1), end=' ')
	# print()

	"""
	for i in range(5000000):
		if is_palin(str(i)):
			n = isqrt(i)
			if n*n == i:
				if is_palin(str(n)):
					print(str(i))
	print()"""

	T = int(input())
	for i in range(T):
		A, B = map(int, input().split())
		print('Case #' + str(i+1) + ': ' + str(solve(B) - solve(A-1)))

main()
