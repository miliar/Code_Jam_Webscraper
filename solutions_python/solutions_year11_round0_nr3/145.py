import os

f = open("C-large.in",'r');
g = open("results.dat",'w')
f.readline()

text = f.readlines()
counter = 0

def tobinary(decimal):
	x = []
	while(decimal > 0):
		x.append(decimal % 2)
		decimal = decimal / 2
	return x

for i in range(len(text)/2):
	counter = counter + 1
	n = int(text[2*i].rstrip())
	array = map(int,text[2*i+1].rstrip().split())
	
	arr = map(tobinary, array)
	m = max(map(len, arr))
	binsum = []
	for j in range(m):
		binsum.append(0)
		for number in arr:
			if (len(number) > j and number[j] == 1):
				binsum[j] = (binsum[j] + 1) % 2
	
	possible = True
		
	for j in range(m):
		if (binsum[j] != 0):
			possible = False
	
	if (not(possible)):
		g.write("Case #" + repr(counter) + ": NO\n")
	else:
		g.write("Case #" + repr(counter) + ": " + repr(sum(array) - min(array)) + "\n")

f.close()
g.close()