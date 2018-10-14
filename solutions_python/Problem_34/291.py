#! /usr/bin/env python

input = open("/Users/benzax/code_jam/input.txt",'r')
s = input.readline()


arr = s.split(" ")

L = int(arr[0])
D = int(arr[1])
N = int(arr[2])

words = []

for i in xrange(0,D):
	words.append((input.readline())[:-1])

output = open("/Users/benzax/code_jam/output.txt",'w')

def match(word, letters):
	for i in range(0, len(word)):
		if word[i] not in letters[i]:
			return False
	return True

for i in xrange(1,N+1):

	seq = input.readline()
	index = 0
	letters = []
	for j in range(0,L):
		pos = []
		if seq[index] == '(':
			index+=1
			while seq[index] != ')':
				pos.append(seq[index])
				index+=1
			index += 1
		else:
			pos = [seq[index]]
			index+=1
		letters.append(pos)
	if index != len(seq)-1:
		print "Warning"
		flag = True
	
	count = 0
	for word in words:
		if match(word, letters):
			count+=1
	s = "Case #" + str(i) + ": " + str(count) + "\n"
	output.write(s)

