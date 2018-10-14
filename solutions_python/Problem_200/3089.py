def check_tidy(lis):
	res = False
	for i in range(1, len(lis)):
		if lis[i] >= lis[i-1]:
			res = True
		else:
			res = False
			break
	return res

file = open("input.in","r")
count = file.readline()
output = open("output.txt","w")
for k, line in enumerate(file):
	st = line.split()
	S = st[0]
	l = list(S)
	lis = [int(i) for i in l]
	for i in range((len(lis)-1),-1,-1):
		if (len(lis) == 1):
			break
		tidy_list = check_tidy(lis)
		if tidy_list == True:
			str1 = ''.join(str(e) for e in lis)
			if int(S) >= int(str1):
				break
		if (i==(len(lis)-1)):
			lis[i] = 9
			continue
		if lis[i] > lis[i-1]:
			lis[i] = lis[i]-1
			tidy_list = check_tidy(lis)
			if tidy_list == True:
				str1 = ''.join(str(e) for e in lis)
				if int(S) >= int(str1):
					break
			else :
				lis[i] = 9
		else:
			if i == 0 and lis[i] > 0:
				lis[i] = lis[i] -1 
			else:
				lis[i] = 9
	if lis[0] == 0:
		lis.pop(0)
	last = ''.join(str(e) for e in lis)
	output.write("Case #" + str(k+1) +": " + last + "\n")
output.close()