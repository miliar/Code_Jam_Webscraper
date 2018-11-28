import sys
T = int(raw_input())

for _ in range(0, T):
	r1 = int(raw_input())
	row1 = []
	for i in range(0, 4):
		a = [int(j) for j in raw_input().split()]
		if i + 1 == r1:
			row1 = a
	
	r2 = int(raw_input())
        row2 = []
        for i in range(0, 4):    
                a = [int(j) for j in raw_input().split()]
                if i + 1 == r2:
                        row2 = a
	
	number = list(set(row1) & set(row2))
	sys.stdout.write("Case #" + str(_ + 1) + ": ")
	if len(number) == 0:
		print "Volunteer cheated!"

	elif len(number) > 1:
		print "Bad magician!"
	
	else:
		print number[0]
