from random import randint

def isReady(s):
	return not ('-' in s)


def flip(s):
	t = ''
	for p in s:
		if p == '+':
			t += '-'
		else:
			t += '+'

	return t


def magic(s, k, n):
	i = 0
	j = len(s)
	a = ''
	if isReady(s):
		return n

	if k > len(s):
		return -1

	for p in s:
		if p == '+':
			i += 1
		else:
			break

	for p in range(j-1, -1, -1):
		if s[p] == '+':
			j -= 1
		else:
			break

	if j - i < k:
		# if k + i < len(s):
		# 	a = s[i:k+i]
		# else:
		# 	while i > 0:
		while j < len(s):
			j += 1
			if j - i >= k:
				a = s[i:j]
				break

		if a == '':
			while i > 0:
				i -= 1
				if j - i >= k:
					a = s[i:j]
					break
	else:
		a = s[i:j]

	return cook(a, k, n)

def cook(s, k, n):
	a = flip(s[:k])+s[k:]
	n += 1

	return magic(a, k, n)


def heyy(s, k):
	try:
		n = magic(s, k, 0)
	except RuntimeError:
		return 'IMPOSSIBLE'

	if n < 0:
		return 'IMPOSSIBLE'

	return n


# def generate():
# 	a = randint(3,10)
# 	k = randint(2, a)
# 	t = ''
# 	for i in range(a):
# 		b = randint(0,1)
# 		if b == 0:
# 			t += '-'
# 		else:
# 			t += '+'

# 	print (t, k)

zz = 1

with open('A-small-attempt1.in') as inputFile, open('A-small-attempt1.out','w') as outputFile:
	for line in inputFile:
		hell = line.split(' ')
		outputFile.write('Case #'+str(zz)+': '+str(heyy(hell[0], int(hell[1])))+'\n')
		zz += 1