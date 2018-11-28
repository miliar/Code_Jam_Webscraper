from math import sqrt

result = ''
outfile = open("OutputSmall.txt", "w")

with open("InputSmall.txt") as f:
	content = f.readlines()

totalcases = int(content[0])

for t in range(1,totalcases + 1):
	result = ''
	start = int(content[t].split(' ')[0].replace('\n',''))
	end = int(content[t].split(' ')[1].replace('\n',''))
	cnt = 0
	for i in range(start, end + 1): 
		stringy = str(i)
		if stringy == stringy[::-1]:
			sq = sqrt(i)
			if int(sq) == sq:
				chotu = str(int(sq))
				if chotu == chotu[::-1]:
					cnt = cnt + 1
	outfile.write('Case #' + str(t) + ': ' + str(cnt) + '\n')


