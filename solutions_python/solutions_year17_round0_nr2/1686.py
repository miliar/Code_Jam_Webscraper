import os


with open("b.in", "r+") as f:
	lines = [x.strip() for x in f.readlines()]

answ = ""

for case in range(1, int(lines[0]) + 1):
	num = list(map(int, str(lines[case])))
	idx = 0

	while idx + 1 < len(num) and num[idx] <= num[idx + 1] :
		idx+=1


	if idx + 1 < len(num) : 
		idx2 = idx
		
		while idx2 > 0 and num[idx] == num[idx2 - 1]:
			idx2 -= 1

		if idx2 == 0 and num[idx2] == 1:
			num = [9] * (len(num) - 1)
		else:
			num[idx2]-=1
			idx2+=1
			while idx2 < len(num):
				num[idx2] = 9
				idx2+=1
				

			
	answ += "Case #{0}: {1}\n".format(case, "".join(map(str,num)))		



with open("b.out", "w") as f:
	f.write(answ)
