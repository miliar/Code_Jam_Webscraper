def helper(s, k):
	if len(s) < k:
		if '-' not in s:
			return 0
		return -1
	elif len(s) == k:
		if '-' not in s:
			return 0
		if '+' not in s:
			return 1
		return -1
	elif s[0] == '+':
		return helper(s[1:], k)
	else:
		result = helper(flip_and_move(s,k), k)
		if result == -1:
			return -1
		else:
			return 1 + result

def flip_and_move(s,k):
	y = ''
	for x in range(1,k):
		if s[x] == '+':
			y += '-'
		else:
			y += '+'
	z = y + s[k:]
	return z

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  n, m = input().split(" ") 
  m = int(m)
  count = helper(n, m)
  if count < 0:
  	count = 'IMPOSSIBLE'
  print("Case #{}: {}".format(i, count))


