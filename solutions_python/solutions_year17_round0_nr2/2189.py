def main():
	f = open("B-large.in", "r")
	lines = f.readlines()
	f.close()
	
	
	w = open("outputLarge.txt", "w")
	n = lines[0]

	for i in range(int(n)):
		l = i + 1
		num = int(lines[l])
		w.write("Case #"+str(l)+": "+str(tidyNum(num))+'\n')

	w.close()

def tidyNum(num):
	
	s = list(map(int, list(str(num))))
	# print(s)
	l = len(s)
	if(l == 1):
		return num
	
	result = [0] * l

	# set everything after this index to 9
	boo = False
	index = -1
	for x in range(l):
		j = l - 1 - x
		if(j == 0):
			result[j] = s[j]
		else:
			if s[j] < s[j-1]:
				index = j
				boo = True
				s[j-1] = s[j-1] - 1
			else:
				result[j] = s[j]
	
	if(boo):
		for y in range(index, l):
			result[y] = 9
	
	# print(result)
	# print(''.join(map(str,result)))

	return int(''.join(map(str,result)))
if __name__ == '__main__':
	main()