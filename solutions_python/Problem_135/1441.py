import sys

# get the file
f = open(sys.argv[1])

# how many to examine
count = int(f.readline().strip())

# to list
r = []
for l in f:
	z = l.strip().split()
	r.append([int(x) for x in z])


# use the remaining lines
for i in range(count):
	a = r[(10*i)+r[10*i][0]]
	b = r[(10*i)+5+r[10*i+5][0]]

	c = 0
	ans = 0
	for d in a:
		if d in b:
			c += 1
			ans = d
	if c == 1:
		print("Case #" + str(i+1) + ": " + str(ans))
	elif c == 0:
		print("Case #" + str(i+1) + ": Volunteer cheated!")
	else:
		print("Case #" + str(i+1) + ": Bad magician!") 
		
		
	

