from random import randint

def tidy(s):
	prev = '0'
	for c in s:
		if c < prev:
			return False
		prev = c
	return True

def get_last_tidy(n):
	prev = '9'
	nines = 0
	for i in range(len(n)):
		if n[i] > prev:
			n = "".join(['9' for _ in range(nines)]) + str((int(n[i]) - 1)) + n[i + 1:]
		nines += 1
		prev = n[i]
	return n.rstrip('0')

t = int(input())
for tc in range(t):
	n = input()
	print("Case #{0}: {1}".format(tc+1,get_last_tidy(n[::-1])[::-1]))
