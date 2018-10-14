
def get_happy_side_up(S, K):
	N = len(S)
	i = 0
	cnt = 0
	while i < N-K:
		if S[i] == '+':
			i += 1
		else:
			S = S[:i] + flip(S[i:i+K]) + S[i+K:]
			cnt += 1

	suf = S[N-K:] if N >= K else S
	minusCount = suf.count('-')
	if minusCount == 0:
		return cnt
	elif minusCount == K:
		return cnt+1
	else:
		return -1

# def flip(str, index, size):
# 	s = str[index:size+index]
def flip(s):
	ret = ['+' if c=='-' else '-' for c in list(s)]
	return ''.join(ret)



t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  splits = raw_input().split(" ")
  S, K = splits[0], int(splits[1])
  ans = get_happy_side_up(S, K)
  print "Case #{}: {}".format(i, ans if ans != -1 else "IMPOSSIBLE")



# print get_happy_side_up("---+-++-", 3)
# print get_happy_side_up("--", 3)
# print get_happy_side_up("+++++", 4)
# print get_happy_side_up("---", 4)
# print get_happy_side_up("-+-+-", 4)