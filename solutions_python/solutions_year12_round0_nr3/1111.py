# Program to solve C. Recycled Numbers

def is_recycled_pair(a, b, call):
	astr = str(a)
	bstr = str(b)
	
	if len(astr) != len(bstr) or len(astr) == 1:
		return False
		
	for i in range(1, len(astr)):
		if astr == (bstr[len(astr) - i:] + bstr[:len(astr) - i]):
			return True

	if call == 1:
		return is_recycled_pair(b, a, 2)
	else:
		return False
	
filename = "in.txt"
infile = open(filename, 'r')

outfile = open("output.txt", 'w')


first_line = True
case = 0

for line in infile:
	if first_line:
		first_line = False
		continue
	case += 1
	start = int(line.split(" ")[0])
	end = int(line.split(" ")[1])
	if end <= start:
		outfile.write("Case #" + str(case) + ": 0" + "\n")
		continue
	
	pair_count = 0
	for n1 in range(start, end):
		for n2 in range(n1 + 1, end + 1):
			if is_recycled_pair(n1, n2, 1):
				pair_count += 1
				
	outfile.write("Case #" + str(case) + ": " + str(pair_count) + "\n")

infile.close()
outfile.close()