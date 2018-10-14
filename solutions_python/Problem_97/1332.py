#!/usr/bin/python
import sys
		
data = sys.stdin.readlines()
cases = int(data.pop(0))
case = 1

while (case <= cases):
	temp = data.pop(0).split()
	A = int(temp[0])
	B = int(temp[1])
	sys.stdout.write("Case #" + str(case) + ": ")
	
	m = A
	answer = set()
	while (m <= B):
		M = str(m)
		if len(M) == 1 or M[0] == '0':
			m += 1
			continue
		
		position = len(M) - 1
		while(position > 0):
			temp = M[position::] + M[0:position]
			tInt = int(temp)
			if (tInt <= B and temp != M and temp[0] != '0' and m < tInt):
				t = M + ":" + temp
				answer.add(t)
				answer.add(temp + ":" + M)
			position -= 1
		m += 1
	sys.stdout.write(str(len(answer)/2) + "\n")
	case += 1