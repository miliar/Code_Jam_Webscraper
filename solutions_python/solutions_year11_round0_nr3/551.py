#!/usr/bin/python
import sys		
import itertools

def AddBinWoutCarry(a,b):
	a = a[2:]
	al = len(a)
	b = b[2:]
	bl = len(b)
	out = "0b"
	if al >= bl:
		diff = al -bl
		for i in range(0,al):
			if i < diff:
				out += a[i]
			elif a[i] == "1" and b[i-diff] == "1":
				out += "0"
			else:
				out += str(int(a[i])+int(b[i-diff]))
	else:
		diff = bl -al
		for i in range(0,bl):
			if i < diff:
				out += b[i]
			elif a[i-diff] == "1" and b[i] == "1":
				out += "0"
			else:
				out += str(int(a[i-diff])+int(b[i]))
	return out

def PileSum(pile):
	sum = "0b00"
	for i in range(0,len(pile)):
		sum = AddBinWoutCarry(sum,pile[i])
	return sum

def SumList(l):
	sum = 0
	for i in l:
		sum += i
	return sum
	
def BinToInt(x):
	x = x[2:]
	num = 0
	for j in range(len(x)):
		c = x[j]
		i = int(c)
		num += i * 2**(len(x)-j-1)
	return num
input = sys.argv[1]

input = open(input).read().strip().split("\n")

cases = int(input[0].strip())

result = ""
for i in range(1,cases+1):
	stuff = [bin(int(e)) for e in input[i*2].split(" ")]
	subsets = []
	osubsets = []
	for L in range(1, len(stuff)):
		for subset in itertools.combinations(stuff, L):
			subsets.append(subset)
	for j in range(0,len(subsets)/2):
		osubsets.append((subsets[j],subsets[len(subsets)-j-1]))
	max = 0
	for osubset in osubsets:
		p1 = list(osubset[0])
		p1sum = PileSum(p1)
		p2 = list(osubset[1])
		p2sum = PileSum(p2)
		if BinToInt(p1sum) == BinToInt(p2sum):
			p1 = sum([BinToInt(e) for e in p1])
			p2 = sum([BinToInt(e) for e in p2])
			if p1 > max:
				max = p1
			if p2 > max:
				max = p2
	if max == 0:
		print "Case #"+str(i)+": NO"
	else:
		print "Case #"+str(i)+": " + str(max)
		
	
