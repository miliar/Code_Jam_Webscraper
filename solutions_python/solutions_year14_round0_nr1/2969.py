from sets import Set

f = open("A-small-attempt0.in", "r");

t = int(f.readline());

for i in range(1, t+1):
	row1 = row2 = None;
	
	r = int(f.readline());
	
	for j in range(1, 5):
		if j == r:
			row1 = Set([int(n) for n in f.readline().split(" ")]);
		else:
			f.readline();
	
	r = int(f.readline());
	
	for j in range(1, 5):
		if j == r:
			row2 = Set([int(n) for n in f.readline().split(" ")]);
		else:
			f.readline();
	
	ans = row1.intersection(row2);
	
	if len(ans) == 0:
		print "Case #" + str(i) + ": Volunteer cheated!"
	elif len(ans) == 1:
		print "Case #" + str(i) + ": " + str(ans.pop());
	else:
		print "Case #" + str(i) + ": Bad magician!"
		
f.close();