from math import floor, sqrt

f = open('bullseye.in');
out = open('bullseye.out', 'w')
cases = int(f.readline());

for CASE in range(1, cases+1):
	line = f.readline().split()
	radius = int(line[0])
	paint = int(line[1])
	b = 2*radius - 1
	rings = int(floor((-b + sqrt(b*b+8*paint))/4.0))

	if 2*rings*rings + rings*b > paint:
		rings -= 1

	out.write("Case #{0}: {1}\n".format(CASE, rings))

