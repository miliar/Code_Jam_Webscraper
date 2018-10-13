file = open("input.txt", "r")
file1 = open("output.txt", "w")

pi = 3.14

def func():
	temp = file.readline()
	n  = int(temp)
	aa = 1
	print n
	print
	for i in range(n):
		amount = 0
		temp = file.readline()
		temp = temp.split()
		rt = [int(temp[0]), int(temp[1])]
		initialS = rt[0] * rt[0]
		firstR = rt[0]
		secondR = rt[0] + 1
		while True:
			firstS = firstR * firstR
			secondS = secondR * secondR
			stringS = secondS - firstS
			if stringS > rt[1]:
				break
			rt[1] -= stringS
			amount += 1
			firstR += 2
			secondR += 2
		file1.write("Case #" + str(aa) +": " + str(amount) + 
			"\n")
		print amount
		aa += 1

func()
