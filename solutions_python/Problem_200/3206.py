def main():
	t = int(input())
	for i in range(1, t + 1):
		number = int(input())

		answer = ""
		if isTidy(number):
			answer = number
		else:
			answer = makeTidy(number)

		print("Case #{}: {}".format(i, answer))

def isTidy(input):
	number = str(input)
	for i in range(len(number) - 1):
		if int(number[i]) > int(number[i + 1]):
			return False
	return True

def makeTidy(number):
	string_num = str(number)
	for i in range(len(string_num) - 1, 0, -1):
		if string_num[i] != "9":
			number -= (int(string_num[i]) + 1) * (10 ** (len(string_num) - 1 - i))
			string_num = str(number)
		if(isTidy(number)):
			return number
	return string_num

if __name__ == '__main__':
	main()