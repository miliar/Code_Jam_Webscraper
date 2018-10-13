#!/usr/bin/python
import sys
import copy

def main():
	f = file(sys.argv[1])
	num = int(f.readline())
	
	word = "welcome to code jam"
	
	for i in range(num):
		line = f.readline().strip('\n')
		
		word_seq = buildline(line, word)
		#printseq(word_seq)
		
		num = count(word_seq)
		print 'Case #%d: %04d' % (i+1, num)

	f.close()
	
def count(seq):
	#printseq(seq)
	while True:
		ret = invalid(seq)
		if ret == False:
			break
	
	#printseq(seq)
	return do_count(seq)
	
def do_count(seq):
	if len(seq) == 0:
		return 1

	for i,j in enumerate(seq):
		if len(j) == 0:
			return 0
	
	newseq = [x for x in seq if len(x) != 1]
	#printseq(newseq)
	
	if len(newseq) == 0:
		return 1
	
	cnt = 0
	for x in newseq[0]:
		cnt += count([[x]]+newseq[1:])		
	
	return cnt

	
	
def invalid(seq):
	found = []
	ret = False
	for i,j in enumerate(seq):
		if len(j) == 1:
			found.append((i, j[0]))
	#printseq(found)

	for k,v in found:
		for i in range(0, k):
			length = len(seq[i])
			row = [r for r in seq[i] if r < v]
			seq[i] = row
			if length != len(row):
				ret = True

		for i in range(k+1, len(seq)):
			length = len(seq[i])
			row = [r for r in seq[i] if r > v]
			seq[i] = row
			if length != len(row):
				ret = True
	return ret
			
	
		
def buildline(line, word):
	ret = []
	result = {}
	for i in word:
		if result.has_key(i):
			ret.append(result[i][:])
			continue
		pos = position(i, line)
		ret.append(pos)
		result[i] = pos
	return ret
		
def position(letter, line):
	ret = []
	beg = 0
	while True:
		pos = line.find(letter, beg)
		if pos == -1:
			break
		ret.append(pos)
		beg = pos+1
	return ret

def printseq(seq):
	for i in seq:
		print i
	print '-'*40

if __name__ == "__main__":
	main()
