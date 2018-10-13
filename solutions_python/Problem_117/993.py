import re
import sys

f = open(sys.argv[1], "r")
n = int(f.readline())
for i in range(1,n+1):
	sys.stdout.write("Case #" + repr(i) + ": ")
	lawn = []
	match = re.search("(\d+) (\d+)", f.readline())
	x, y = int(match.group(1)), int(match.group(2))
	for j in range(x):
		list = re.split(" ", f.readline())
		temp = []
		for k in range(y):
			temp.append(int(list[k]))
		lawn.append(temp)
	
	good = True
	for j in range(x):
		for k in range(y):
			vertgood = True
			horgood = True
			for l in range(x):
				if (lawn[j][k] < lawn[l][k]):
					horgood = False
			for l in range(y):
				if (lawn[j][k] < lawn[j][l]):
					vertgood = False
			if not (vertgood or horgood):
				good = False
	if good:
		sys.stdout.write("YES\n")
	else:
		sys.stdout.write("NO\n")