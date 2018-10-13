import math

t = int(raw_input())

'''
stall = list()
stall.append(1)
stall.append(5)
stall.append(2)
stall.append(6)
stall.sort()
print(stall)
#print(max(v1 - v0 for v0, v1 in zip(stall[:-1], stall[1:])))
for v0, v1 in zip(stall[:-1], stall[1:]):
	print(v0, v1, v1-v0)
quit()
'''

for i in range(1, t + 1):
	nstall, people = [int(s) for s in raw_input().split(" ")]
	stall = list()

	stall.append(0)
	stall.append(nstall+1)

	if (nstall == people):
		print "Case #{}: {} {}".format(i, 0, 0)
		continue

	#print("Stall:"+ str(nstall))
	while people != 0:
		# Left/Rigt Space
		ls = 0
		rs = 0
		# Max
		m = 0
		# Left/Right Index
		li = 0
		ri = nstall+1
		# Find Max/Left Index/Right Index
		#print("Looping")
		for v0, v1 in zip(stall[:-1], stall[1:]):
			#print(v0, v1)
			if (m < v1 - v0):
				m = v1 - v0
				li = v0
				ri = v1
		#print("Found", m, li, ri)
		mid = int((ri-li)/2)+li
		ls = mid-li-1
		rs = ri-mid-1
		# Allocate Person
		stall.append(mid)
		people = people - 1
		stall.sort()
		# Information

	#quit()

	# Set the Guards
	#stall[0] = True
	#stall[nstall+1] = True
	
	#print(nstall, people)

	print "Case #{}: {} {}".format(i, max(ls, rs), min(ls, rs))