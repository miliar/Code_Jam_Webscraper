
infile = open("B-large.in", "r")
outfile = open("outfile.txt", "w")

def checktidy(number):
	dig_list = []
	while number/10 > 0:
		dig_list.append(number%10)
		number = number/10
	dig_list.append(number)
	s_list = list(reversed(sorted(dig_list)))
	if dig_list == s_list:
		del dig_list[:]
		return True
	else:
		del dig_list[:]		
		return False

def propogate(digit_listB):
	digit_listB = list(reversed(digit_listB))
	fin = 0
	for idx, item in enumerate(digit_listB):
		if idx == len(digit_listB)-1:
			break
		if digit_listB[idx] <= digit_listB[idx+1]:
			continue
		else:
			digit_listB[idx] = digit_listB[idx] - 1
			while idx < len(digit_listB)-1:
				idx = idx + 1
				digit_listB[idx] = 9
			for item in digit_listB:
				fin = fin*10 + item
			return fin
	del digit_listB[:]
	return fin

def getnext(number):
	digit_list = []
	while number/10 > 0:
		digit_list.append(number%10)
		number = number/10
	digit_list.append(number)
	ans = propogate(digit_list)
	del digit_list[:]
	return ans

def mainfunc(number, idx):
	if checktidy(number):
		outfile.write("Case #"+str(idx)+": "+str(number)+"\n")
		return
	else:
		mainfunc(getnext(number), idx)

for idx,line in enumerate(infile):
	if idx == 0:
		continue
	num = int(line.split()[0])
	mainfunc(num, idx)

infile.close()
outfile.close()	
