def main():
	file = open("e.txt","r")
	inp = file.read().split("\n")
	print(inp)
	num = 0
	for str in inp:
		num+=1
		slist = [int(i) for i in str[2:]]
		maxl = int(str[0])
		if len(slist) == 1:
			print("Case #{}: {}".format(num,0))
		else:
			level = 1
			current = slist[0]
			invite = 0
			while True:
				if current >= level:
					if level == maxl:
						print("Case #{}: {}".format(num,invite))
						break
					current += slist[level]
					level += 1
				else:
					invite+=1
					current+=1
				
main()