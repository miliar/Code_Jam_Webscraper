#generated a list of fair and square numbers using C++

fairsquarenums = [0, 1, 4, 9, 121, 484, 10201, 12321, 14641, 
	40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 
	104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 
	10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 
	1000002000001, 1002003002001, 1004006004001, 1020304030201, 
	1022325232201, 1024348434201, 1210024200121, 1212225222121, 
	1214428244121, 1232346432321, 1234567654321, 4000008000004, 
	4004009004004]

from sys import argv

script, in_file, out_file = argv

read_from = open(in_file, 'r')
write_to = open(out_file, 'w')

num_cases = int(read_from.readline())

for i in range(num_cases):
	count = 0
	endpoints = read_from.readline().split()
	lowpoint = int(endpoints[0])
	highpoint = int(endpoints[1])

	for num in fairsquarenums:
		if num > highpoint:
			break
		if lowpoint <= num and highpoint >= num:
			count += 1

	write_to.write("Case #" + str(i + 1) + ": " + str(count) + '\n')

read_from.close()
write_to.close()
