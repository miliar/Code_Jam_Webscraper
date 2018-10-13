def main():
	first = True
	t = 0
	datas =[]
	with open("codejam.txt","r") as lines:
		for line in lines:
			if first:
				t = int(line)
				first = False
			else:
				datas.append(line.strip("\n"))
		id = 0
		for data in datas:
			zero = False
			temp = list(data)
			id += 1
			for number in data:
				if number == '0':
					zero = True
					break
			if zero:
				for i in range(len(temp)):
					if i == 0:
						temp[i]=str(int(temp[i])-1)
					else:
						temp[i]='9'
			tramp = "".join(temp)
			for i in range(int(tramp),0,-1):
				if check(i):
					print("Case #{}: {}".format(id,i))
					break
			

def check(i):
	test = str(i)
	if len(test) == 1:
		return True
	else:
		for j in range(len(test)-1):
			if int(test[j]) > int(test[j+1]):
				return False
	return True


if __name__ == "__main__":
	main()