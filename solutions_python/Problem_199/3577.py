def main():
	first = True
	t = 0
	datas =[]
	organized =[]
	steps = 0
	with open("codejam.txt","r") as lines:
		for line in lines:
			if first:
				t = int(line)
				first = False
			else:
				datas.append(line.strip("\n"))
	for data in datas:
		organized.append(data.split(" "))
	i=0

	for line in organized:
		i += 1
		pancakes = line[0]
		row = int(line[1])
		steps = solver(pancakes,row)
		print("Case #{}: {}".format(i,steps))

def check(pancakes,side):
	if all(pancake == side for pancake in pancakes):
		return True
	return False

def solver(pancakes,rows):
	steps = 0
	im_test =0
	pan = list(pancakes)
	while check(pan,'+') == False:
		for i in range(len(pan) - rows + 1):
			if pan[i] == '-':
				for j in range(rows):
					if pan[i+j] == '-':
						pan[i+j] = '+'
					else:
						pan[i+j] = '-'
				i += (rows-1)
				steps += 1
		im_test += 1
		if im_test > len(pancakes):
			return "IMPOSSIBLE"
	return steps


if __name__ == "__main__":
	main()