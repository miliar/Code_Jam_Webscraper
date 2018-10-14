import collections
from collections import *
f = open('input.txt', 'r')
amount = f.readline()
amount = int(amount)
qw = 0
string = ''
money =0
for qw in range(amount):

	
	# R Times per day
	# K people at once
	# N used for groups
	temp1 = f.readline().split(' ')
	R = int(temp1[0])
	K = int(temp1[1])
	N = int(temp1[2])
	
	#the groups
	groups = f.readline().split(' ')
	groups = deque(groups)
	mm = 0;
	for a in groups:
		groups[mm] = int(a)
		mm = mm+1
	i = 0
	if sum(groups) <= K:
		money += R*sum(groups)
	else:
		for i in range(R):
			j = 0
			sums = 0
			no = 0
			while K >= sums and no == 0:
				if j >= N:
					no = 1
					print "no"
				else:
					sums = sums + int(groups[j])
					print sums
					j = j+1
			#now to subtract one
			sums = sums - int(groups[j-1])
			money = money + sums
			groups.rotate(-(j-1))
			
	string+="Case #" + str(qw+1) + ": "+str(money)+"\n"
	print "Case #" + str(qw+1) + ": "+str(money)
	money = 0

f = open('out.txt', 'w')
f.write(string)
