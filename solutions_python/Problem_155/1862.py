import fileinput
import pdb

def ovation(people, lastindex):
	total = 0
	add = 0
	for i in range(lastindex+1):
		total += int(people[i])
		if total <= i:
			add += i-total+1
			total += i-total+1
		if total > lastindex+1:
			break
	return add


T = 0
for line in fileinput.input():
	if T == 0:
		T += 1
		continue
	import pdb;pdb.set_trace
	input = line.split(" ")
	lastindex = int(input[0])
	people = list(input[1])
	ans = ovation(people, lastindex)
	
	print "Case #{}: {}".format(T,ans)
	T += 1