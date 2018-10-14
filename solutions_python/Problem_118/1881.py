import math

def square(x):
	return x*x

infile = open('C-small-attempt1.in','r')
outfile = open('out.txt','w')

tests = int(infile.readline())

for i in range(tests):
    numbers = infile.readline().split()
    A = int(numbers[0])
    B = int(numbers[1])

    result = 0
    upper = int(math.sqrt(B))

    for j in range(1, upper+1):
	tmp = str(j)
	if (tmp == tmp[::-1]):
		num = int(math.pow(j, 2))
		if (num >= A):
			string = str(num)
			if (string == string[::-1]):
				result += 1

    outfile.write('Case #' + str(i+1) + ': ' + str(result) + '\n')

infile.close()
outfile.close()

