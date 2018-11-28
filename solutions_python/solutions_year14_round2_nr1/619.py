def comp(str1, str2):
	i = 0;
	j = 0;
	count = 0

	
	while True:
		flag = 0
		if str1[i] == str2[j]:
			if i+1<len(str1) and j+1<len(str2):
				i += 1
				j += 1
				flag = 1
			elif i+1 < len(str1):
				i +=1
				count +=1
				flag =1
			elif j+1 < len(str2):
				j += 1
				count += 1
				flag = 1
		else:
			if str1[i] == str1[i-1]:
				if i+1 < len(str1):
					i += 1
					flag = 1
					count += 1
			if str2[j] == str2[j-1]:
				if j+1 < len(str2):
					j += 1
					flag = 1
					count +=1
		if flag == 0:
			if i == len(str1)-1 and j == len(str2)-1 and str1[i] == str2[j]:
				return count
			else:
				return -1

def main():
	fin = open('A-small-attempt1.in')
	fout = open('out.txt', 'w')

	cases = int(fin.readline())

	for case in range(cases):
		print case
		strlist = []
		mincount = -1
		count = 0
		temp = 0
		N = int(fin.readline())
		for i in range(N):
			strlist.append(fin.readline().replace('\n', ''))
		for i in range(N):
			count = 0
			for j in range(N):
				if i != j:
					temp = comp(strlist[i],strlist[j])
					if temp == -1:
						count = -1
						break
					else:
						count += temp
			if count == -1:
				mincount = -1
				break;
			if mincount == -1 or mincount > count:
				mincount = count

		if mincount == -1:
			fout.write("Case #"+str(case+1)+": Fegla Won\n") 
		else:
			fout.write("Case #" + str(case+1)+": "+str(mincount) + "\n")
	fin.close()
	fout.close()

main()