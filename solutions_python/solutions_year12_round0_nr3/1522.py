input_file = open("C-small.in")
output_file = open("C-small.out", "w")

input_file.readline()

count = 0

for line in input_file:
	count += 1

	pairs = 0
	
	a_str, b_str = line.split()
	a, b = int(a_str), int(b_str)

	while a<b:
		n, m = a, a+1

		while m<=b:
			n_str, m_str = str(n), str(m)

			for i in range(len(n_str)-1):
				recycle_n = n_str[i+1:] + n_str[:i+1]

				if recycle_n==m_str:
					pairs += 1

			m +=1

		a += 1

	output_file.write("Case #" + str(count) + ": " + str(pairs) + "\n")

input_file.close()
output_file.close()