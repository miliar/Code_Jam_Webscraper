def flip(s, i, k):
	flipped_part = ""
	for j in range(i, i+k):
		if s[j] == '+':
			flipped_part += '-'
		else:
			flipped_part += '+'
	return s[:i] + flipped_part + s[i+k:]

def has_minus(s):
	for c in s:
		if c == '-':
			return True
	return False

def get_flips(s, k):
	last = len(s) - k
	n_flips = 0
	for i in range(last + 1):
		if s[i] == '-':
			s = flip(s, i, k)
			n_flips += 1
	return n_flips if not has_minus(s) else "IMPOSSIBLE"





if __name__ == "__main__":
	N = int(raw_input())
	for i in range(1, N+1):
		line = raw_input().split(' ')
		print "Case #{}: {}".format(i, get_flips(line[0], int(line[1])))
