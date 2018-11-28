#!/usr/bin/python

def mowlawn(m,n,r):
	answer = ""

	irows = []
	
	for rows in r:
		irows.append(map(int,rows.split(" ")))
		
	# print irows

	icols = []
	
	for j in range (0,n):
		icols.append([])
		for rows in irows:
			icols[j].append(rows[j])

	# print icols

	for column in icols:
		# print column
		cmax = max(column)
		i = 0
		for element in column:
			if(element < cmax):
				if(element < max(irows[i])):
					answer = "NO"
			i = i + 1

	if(answer == ""):
		answer = "YES"

	return answer


def truncatenewline(str):
	return str[0:len(str)-1]


f = open('input.txt');
o = open('output.txt','w')

stuff = f.readlines()
stuff = map(truncatenewline,stuff)

# print stuff

testcases = int(stuff[0])
j = 1

for i in range(0,testcases):
	
	m = int(stuff[j].split(" ")[0])
	n = int(stuff[j].split(" ")[1])
	

	r = []
	for k in range(0,m):
		r.append(stuff[j+k+1])
	print r

	o.write("Case #" + str(i+1) + ": " + mowlawn(m,n,r) + "\n") 
	j = j + m + 1
	