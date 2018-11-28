import sys

file = sys.argv[1]
text = open(file)
lines = text.readlines()

cases = lines.pop(0);

for i in range(int(cases)):
	a = lines.pop(0)
	r = int(a.split(' ')[0])
	t = int(a.split(' ')[1])
	num_circles, radius = 0, r
	while t>0:
		ml = ((radius+1)**2) - ((radius)**2) 
		if ml <= t:
			num_circles+=1
			t-=ml
		else:
			break
		radius+=2
	print("Case #{0}: {1}".format(i+1, num_circles))