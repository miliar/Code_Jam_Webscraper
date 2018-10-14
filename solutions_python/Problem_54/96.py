file = open('in.txt')
file2 = open('out.txt', 'w')
line = file.readline()
cases = int(line)

def gcd(a, b):
	if a == 0:
		return b
	else:
		return gcd(b % a, a)

for x in range(1, cases+1):
	line = file.readline()
	parts = line.split(' ')
	numbers = [int(P) for P in parts]
	n = numbers[0]
	g = 0
	last = numbers[1]
	for y in range(1, len(numbers)):
		current = numbers[y]
		if current < last:
			g = gcd(g, last - current)
		else:
			g = gcd(current - last, g)
	if g ==0:
                output = "Case #%d: %d\n" % (x, 0)
                file2.write(output)
        else:
                if (last % g) == 0:
                        output = "Case #%d: %d\n" % (x, 0)
                        file2.write(output)
                else:
                        output = "Case #%d: %d\n" % (x, g - (last % g))
                        file2.write(output)
file2.close()
