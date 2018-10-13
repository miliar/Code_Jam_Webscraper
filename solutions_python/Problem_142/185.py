def pop_char(s, ch):
	count = 0
	while s and s[0] == ch:
		count += 1
		s = s[1:]
	return count

def min_move(l):
	l.sort()
	if l[0] == 0:
		return None
	count = 0
	ll = len(l)
	for i in range(ll // 2):
		count += l[ll - 1 - i] - l[i]
	return count

def solver():
	n = int(input())
	ss = [input() for i in range(n)]
	count = 0
	while ss[0]:
		ch = ss[0][0]
		counts = [0] * n
		for i in range(n):
			while ss[i] and ss[i][0] == ch:
				counts[i] += 1
				ss[i] = ss[i][1:]
		local_count = min_move(counts)
		#print(ss)
		if local_count == None:
			return None
		count += local_count
	if any(ss) == True:
		return None
	return count

def main():
	t = int(input())
	for i in range(1, t + 1):
		number = solver()
		print("Case #{:d}: {:s}".format(i, str(number) if number != None else "Fegla Won"))

if __name__ == "__main__":
	main()