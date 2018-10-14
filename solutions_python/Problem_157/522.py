import math
import time

stime = time.time()

dic = {'11':'1', '1i':'i', '1j':'j', '1k':'k', 'i1':'i', 'ii':'1', 'ij':'k', 'ik':'j', 'j1':'j', 'ji':'k', 'jj':'1', 'jk':'i', 'k1':'k', 'ki':'j', 'kj':'i', 'kk':'1'}
signDic = {'11':1, '1i':1, '1j':1, '1k':1, 'i1':1, 'ii':-1, 'ij':1, 'ik':-1, 'j1':1, 'ji':-1, 'jj':-1, 'jk':1, 'k1':1, 'ki':1, 'kj':-1, 'kk':-1}
signDic2 = {'11':1, '1i':-1, '1j':-1, '1k':-1, 'i1':1, 'ii':1, 'ij':-1, 'ik':1, 'j1':1, 'ji':1, 'jj':1, 'jk':-1, 'k1':1, 'ki':-1, 'kj':1, 'kk':1}

def red(tupel, char):

	sign = tupel[0]
	string = tupel[1] + char
	while len(string) > 1:
		sign *= signDic[string[:2]]
		string = dic[string[:2]] + string[2:]
	return (sign, string)


def inc(tupel, char):

	sign = tupel[0]
	string = tupel[1] + char
	if len(string) > 1:
		sign *= signDic2[string[:2]]
		string = dic[string[:2]]
	return (sign, string)


def find_i(chars):

	found = False
	sign = 1
	while len(chars) > 3 and found == False:
		sign *= signDic[chars[:2]]
		newChar = dic[chars[:2]]
		chars = newChar + chars[2:]
		if newChar == 'i' and sign == 1:
			found = find_j(chars[1:])
			break
	return found or (chars[0] == 'i' and sign == 1 and find_j(chars[1:]))


def find_j(chars):

	found = False
	sign = 1
	while len(chars) > 2 and found == False:
		sign *= signDic[chars[:2]]
		newChar = dic[chars[:2]]
		chars = newChar + chars[2:]
		if newChar == 'j' and sign == 1:
			found = find_k(chars[1:])
			break
	return found or (chars[0] == 'j' and sign == 1 and find_k(chars[1:]))


def find_k(chars):

	sign = 1
	while len(chars) > 1:
		sign *= signDic[chars[:2]]
		newChar = dic[chars[:2]]
		chars = newChar + chars[2:]
	return chars[0] == 'k' and sign == 1


def solve(charCount, repeats, chars):

	chars = repeats * chars
	if len(chars) < 3:
		return "NO"
	if ('i' not in chars and 'j' not in chars) or ('i' not in chars and 'k' not in chars) or ('j' not in chars and 'k' not in chars):
		return "NO"
	return "YES" if find_i(chars) else "NO"

def solve2(charCount, repeats, chars):

	chars = repeats * chars
	if len(chars) < 3:
		return "NO"
	if ('i' not in chars and 'j' not in chars) or ('i' not in chars and 'k' not in chars) or ('j' not in chars and 'k' not in chars):
		return "NO"
	a = (1, '')
	for i in range(1, len(chars) - 1):
		a = red(a, chars[i-1])
		if (a[1] != 'i'):
			continue
		b = (1, '')
		c = (1, '')
		c = red(c, chars[i+1:])
		found_k = False
		for j in range(i + 1, len(chars)):
			b = red(b, chars[j-1])
			if ((a[0] * b[0] * c[0]) == 1 and a[1] == 'i' and b[1] == 'j' and c[1] == 'k'):
				return "YES"
			if c[1] == 'k':
				found_k = True
			c = inc(c, chars[j])
		if not found_k:
			return "NO"
	return "NO"


name = "testc"
name = "C-small-attempt3"
fi = open(name + ".in", "r")

fout = open(name + ".out", "w")

numTestCases = int(fi.readline())
print "#TestCases: ", numTestCases

for i in range(0, numTestCases):
	line = fi.readline().strip().split(" ")
	line2 = fi.readline().strip()
	line = map(int, line)
	cachedLine2 = line2

	fout.write("Case #" + str(i + 1) + ": " + solve(line[0], line[1], line2) + "\n")
	print "Case #" + str(i + 1) + ": " + solve(line[0], line[1], cachedLine2)

print "Time:", time.time() - stime
fi.close()
fout.close()