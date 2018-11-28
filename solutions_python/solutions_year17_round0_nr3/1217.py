import math
f = open("C-small-2-attempt4.in", 'r')
count = 0
content = f.read()
content = content.splitlines()
out = open("small2-out", 'w')

def choose(stalls):
	if stalls%2 == 1:
		return int((stalls-1)/2), int((stalls-1)/2)
	else:
		return int((stalls-1)/2+1), int((stalls-1)/2)


for l in content:
	if count == 0:
		count += 1
		continue
	l = l.split(' ')
	stall = int(l[0])
	people = int(l[1])
	if people == 1:
		maxs, mins = choose(stall)
		out.write("Case #" + str(count) + ": " + str(maxs) + " " + str(mins) + "\n")
		count += 1
		continue

	level = int(math.log(people, 2))
	pos = people
	for i in range(level):
		pos -= 1<<i
	ocu = people-pos
	mm = (stall - ocu)%(1<<level)
	mn = int((stall - ocu)/(1<<level))
	if(pos > mm):
		maxs, mins = choose(mn)
	else:
		maxs, mins = choose(mn+1)
	
	out.write("Case #" + str(count) + ": " + str(maxs) + " " + str(mins) + "\n")
	#out.write("Case #" + str(count) + ': ' + str(int(s)) + '\n')
	count += 1

