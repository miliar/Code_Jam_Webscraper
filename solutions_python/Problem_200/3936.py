def parser():
    t = int(raw_input()) 
    numbers = []
    for i in range(1, t + 1):
        a = raw_input()
        numbers.append(a)
    return numbers

def is_tidy(num):
	if len(num) == 1:
		return True
	for i in range(0, len(num) - 1):
		if int(num[i]) > int(num[i + 1]):
			return False
	return True


def brute_find_tidy(num):
	tmp = num
	while(True):
		if(is_tidy(tmp)):
			return tmp
		tmp = str(int(tmp) - 1)

def smart_find_tidy(num):
	if len(num) == 1:
		return num
	occur = 0
	res = ""
	for i in range(0, len(num) - 1):
		if (int(num[i]) > int(num[i + 1])):
			if(occur > 0):
				return res[:-occur] + str(int(num[i]) - 1) + ((len(num) - i - 1 + occur) * '9')
			else:
				return res + str(int(num[i]) - 1) +  ((len(num) - i - 1) * '9')
		elif (int(num[i]) == int(num[i + 1])):
			occur = occur + 1
			res = res + num[i]
		else:
			occur = 0
			res = res + num[i]
	return num 

def printer(result):
	for i in range(1, len(result) + 1):
		print "Case #" + str(i) + ": " + str(int(result[i-1]))

def main():
	numbers = parser()
	res = []
	for i in range (0, len(numbers)):
		res.append(smart_find_tidy(numbers[i]))

	printer(res)

if __name__ == "__main__":
    main()