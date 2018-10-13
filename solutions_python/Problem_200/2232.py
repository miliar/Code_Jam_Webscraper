file_in = open("B-small-attempt0.in", "r")
file_out = open("B-small-attempt0.out", "w")

T = int(file_in.readline().rstrip())

for i in range(T):
	num = map(int, list(file_in.readline().rstrip()))
	
	if all(num[i] <= num[i+1] for i in xrange(len(num)-1)):
		file_out.write("Case #" + str(i+1) + ": " + ''.join(map(str,num)) +"\n")

	else:
		reversed_num = num[::-1]
		for ind in range(len(reversed_num)):	
			if ind<len(num)-1:
				if reversed_num[ind]<reversed_num[ind+1]:
					for t in range(ind+1):
						reversed_num[t] = 9
					reversed_num[ind+1] -= 1
		
		num = reversed_num[::-1]
		for d in range(len(num)):
			if num[d]==0:
				num = num[1:]
			else:
				break

		file_out.write("Case #" + str(i+1) + ": " + ''.join(map(str,num)) +"\n")

file_in.close()
file_out.close()
