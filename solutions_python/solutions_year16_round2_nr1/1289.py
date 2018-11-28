#!/usr/bin/env python

debug=0

def compute(S):
	answer=[]
	d={}
	for char in list(S):
		if char in d.keys():
			d[char]=d[char]+1
		else:
			d[char]=1
	if debug > 5:
		print "dict(S):",d
	#g:eight
	#u:four
  #w:two
	#x:six
	#z:zero
	#f:five
	#h:three
	#o:one
	#s:seven
	#e:nine
	sequence=["EIGHT","FOUR","TWO","SIX","ZERO","FIVE","THREE","ONE","SEVEN","NINE"]
	numbers={"EIGHT":8,"FOUR":4,"TWO":2,"SIX":6,"ZERO":0,"FIVE":5,"THREE":3,"ONE":1,"SEVEN":7,"NINE":9}
	for digit in sequence:
		e={}
		for char in list(digit):
			if char in e.keys():
				e[char]=e[char]+1
			else:
				e[char]=1
		count=len(S)
		for char in e.keys():
			if char in d.keys():
				count=min([count,d[char]/e[char]])
			else:
				count=0
		if debug > 5:
			print "dict(digit):",e
			print count
		if count > 0:
			for char in e.keys():
				d[char]=d[char]-count*e[char]
		for i in range(count):
			answer.append(str(numbers[digit]))
	answer.sort()
	if max(d.values())>0:
		print "ERROR:",d
	return "".join(answer)
	

def solve(infilename):
	infile=open(infilename,'r')
	line=infile.readline()
	T=int(line)
	if debug > 10:
		print 'T:',T
		digits=["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]		
		d={}
		for digit in digits:
			for char in list(digit):
				if char in d.keys():
					d[char]=d[char]+1
				else:
					d[char]=1
		print d
		digits=["ONE", "THREE", "FIVE", "SEVEN", "NINE"]		
		d={}
		for digit in digits:
			for char in list(digit):
				if char in d.keys():
					d[char]=d[char]+1
				else:
					d[char]=1
		print d

	#iterate
	for index in range(T):
		S=infile.readline().rstrip()
		if debug > 10:
			print 
			print 'S:',S
		answer = compute(S)
		print 'Case #%(index)d: %(answer)s' % {"index":index+1,"answer":answer}
	infile.close()
	return

if __name__ == "__main__":
	import sys
	if len(sys.argv) > 1:
		solve(sys.argv[1])
	else:
		solve('A-example.in')
