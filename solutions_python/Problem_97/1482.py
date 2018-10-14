def main(test_cases, data):
	for t in range(test_cases):
		init = data[t][0]
		final = data[t][1]

		arr = []
		append = arr.append

		for x in range(init, final+1):
			append(x)

		ctr = 0;

		size = final - init + 1

  		for i in range(size):
                	temp = map(int, str(arr[i]))
                	digits = len(temp)

			join = ''.join

			for j in range(digits):
				store = temp[-j:] + temp[:-j]
				new = int(join(map(str, store)))

				if new < arr[0] or new > arr[size-1]:
					continue
		
				if new in arr[i+1:]:
					ctr+=1

		print "Case #{}: {}".format(t+1, ctr)	

infile = open('input.txt', 'r')

test_cases = [int(x) for x in infile.readline().split()][0]
data = [[int(x) for x in line.split()] for line in infile]

main(test_cases, data)

