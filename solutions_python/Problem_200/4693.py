#! /usr/bin/python3

def checktidy(test_num):
	x = list(str(test_num))
	x.sort()
	w = int(''.join(x))
	diff = test_num - w
	if diff == 0:
		return True
	else:
		return False


def finalTidy(num):
	if (num < 10):
		return num
	for i in range(1, num+1):
		x = checktidy(i)
		if x == True:
			t = i
	return t



def main():
	number_test_cases = int(input())
	z = []
	flag = 1
	for i in range(number_test_cases):
		z.append(int(input()))
	for i in z:
		c = finalTidy(i)
		print("Case #{}: {}".format(flag,c))
		flag = flag + 1

if __name__ == '__main__':
	main()