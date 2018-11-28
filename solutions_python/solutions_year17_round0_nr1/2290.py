def swap(a):
	a = [-i for i in a]
	return a
		
file1 = open("large-2.in")
file2 = open("large.out",'w+')
file1.readline()
j = 1
pattern = {'+':1, '-':-1}
for line in file1:
	a = line.split(' ')
	K = int(a[1])
	ori = list(a[0])
	ori = [pattern[x] if x in pattern else x for x in ori]
	res = 0
	loc = 0
	for i in ori:
		if(i == -1 and loc+K < len(ori)+1):
			ori[loc:loc+K] = swap(ori[loc:loc+K])
			res += 1
		elif(i == -1 and loc+K >= len(ori)+1):
			res = "IMPOSSIBLE"
		loc += 1
	file2.writelines("Case #{0}: {1}\n".format(j,res))
	j += 1
	
file2.close()
