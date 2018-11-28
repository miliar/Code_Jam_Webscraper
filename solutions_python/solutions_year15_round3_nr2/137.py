import math
import itertools

def possibleOverlap(word):
	count = 0
	for i in range(1, len(word)):
		tcount = 0
		for j in range(0, i):
			if word[j] == word[-i + j]:
				tcount += 1
		if tcount == i:
			count = tcount

	return count

def occurrences(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            return count

def possibleBananas(target, s):
	return 1 + (s - len(target)) / (len(target) - possibleOverlap(target))

def freqs(keys, target):
	f = {}
	for key in target:
		f[key] = keys.count(key) / (1.0 * len(keys))
	return f

def solve(s, keys, target):

	if len(list(set(target) - set(keys))) > 0:
		return 0.0
	else:
		#ov = possibleOverlap(target)
		#freq = freqs(keys, target)
		count = 0
		poss = 0
		for p in itertools.product(keys, repeat=s):
			poss += 1
			count += occurrences(''.join(p), target)
			#print ''.join(p), target
		#print poss, count
		return possibleBananas(target, s) - count / (1.0 * poss)



name = "B-small-attempt0"
fi = open(name + ".in", "r")

fout = open(name + ".out", "w")

numTestCases = int(fi.readline())
print "#TestCases: ", numTestCases

for i in range(0, numTestCases):
	line0 = fi.readline().strip().split(" ")
	line0 = map(int, line0)
	keys = fi.readline().strip()
	target = fi.readline().strip()

	fout.write("Case #" + str(i + 1) + ": " + str(solve(line0[2], keys, target)) + "\n")
	#print "Case #" + str(i + 1) + ": " + str(solve(line0[2], keys, target))

fi.close()
fout.close()