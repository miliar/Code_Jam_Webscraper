from math import sqrt

f = open('C-small.txt')
no_cases = int(f.readline().strip())
f_write = open('output.txt', 'w')

for case_count in range(no_cases):
	a, b = f.readline().strip().split()
	a, b = int(a), int(b)
	
	no_count = 0

	for i in range(a, b+1):
		if str(i) == str(i)[::-1]:
			no_sqrt = int(sqrt(i))
			
			if pow(no_sqrt, 2) == i:
				if str(no_sqrt) == str(no_sqrt)[::-1]:
					no_count += 1

	
	f_write.write("Case #" + str(case_count+1) + ": ")
	f_write.write(str(no_count))
	f_write.write('\n')


f_write.close()
f.close()