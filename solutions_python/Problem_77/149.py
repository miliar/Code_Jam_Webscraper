import os

f = open("D-large.in",'r');
g = open("results.dat",'w')
f.readline()

text = f.readlines()
counter = 0

for i in range(len(text)/2):
	outofplace = 0
	counter = counter + 1
	n = int(text[2*i].rstrip())
	array = map(int,text[2*i+1].rstrip().split())
	
	for j in range(n):
			if (array[j] != j+1):
				outofplace = outofplace + 1
				
	g.write("Case #" + repr(counter) + ": " + repr(outofplace) + "\n")
			
f.close()
g.close()