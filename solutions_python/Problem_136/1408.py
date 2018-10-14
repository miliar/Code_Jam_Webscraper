import sys

# get the file
f = open(sys.argv[1])

count = int(f.readline().strip())

# to list
r = []
for l in f:
	r.append([float(x) for x in l.strip().split()])

for i in range(count):
	bonus = r[i][0]
	delta = r[i][1]
	goal = r[i][2]
	rate = 2
	status = [0.0, goal / rate] # time to get here, time to finish
	prevstatus = [999999999.0, 999999999.0]

	while (status[0] + status[1]) < (prevstatus[0] + prevstatus[1]):
		prevstatus[0] = status[0]
		prevstatus[1] = status[1]
		status[0] = prevstatus[0] + (bonus / rate)
		rate += delta
		status[1] = goal / rate

	print("Case #" + str(i+1) + ": %.7f" % (prevstatus[0] + prevstatus[1]))
