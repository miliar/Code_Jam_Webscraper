import sys

cache = {}

for i in range(0,31):
	cache[i] = {"surprising":0,"not surprising":0}

	# very naive but it works, huh ?
	for j in range(0,11):
		for k in range(j,min(11,j+3)):
			for l in range(k,min(11,j+3)):
				if j+k+l == i:
					cache[i]["surprising"] = max(cache[i]["surprising"],l)
					if (l-j <= 1):
						cache[i]["not surprising"] = max(cache[i]["not surprising"],l)

number = int(sys.stdin.readline())
myReturn = ""

for i in range(0,number):
	line = sys.stdin.readline().split()

	surprising = int(line[1])
	points = int(line[2])

	notes = [int(note) for note in line[3:]]
	notes.sort()
	notes.reverse()
	total = 0

	while total < len(notes) and cache[notes[total]]["not surprising"] >= points:
			total += 1
	while total < len(notes) and surprising > 0 and cache[notes[total]]["surprising"] >= points:
			total += 1
			surprising -= 1

	myReturn += "Case #"+str(i+1)+": "+str(total)+"\n"

print myReturn