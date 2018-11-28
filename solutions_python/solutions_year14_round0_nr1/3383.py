def bar(f):
	first = int (f.readline())

	for i in range(1, first):
		f.readline()

	first_in = f.readline().split()

	for i in range(first, 4):
		f.readline()

	return (first, first_in)
		


def solve(f, n):
	(first, first_in) = bar(f)
	(second, second_in) = bar(f)
	
	c = 0
	k = -1
	
	for i in range (0, 4):
		for j in range(0, 4):
			if (first_in[i] == second_in[j]):
				c = c + 1
				k = first_in[i]
				if (c==2):
        				print "Case #" + str(n)+": Bad magician!"
					return
	if (c==1):
		print "Case #"+str(n)+": "+str(k)
	else:
		print "Case #"+str(n)+": Volunteer cheated!"
	return
		



def foo() :
	f = open('d://A-small-attempt0.in', 'r')
	num_cases = int(f.readline())
	for i in range (0, num_cases):
		solve(f, i+1)

foo()
