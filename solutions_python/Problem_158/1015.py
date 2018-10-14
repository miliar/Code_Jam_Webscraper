def compute(n, length, width):
	if (length * width) % n != 0:
		return 'RICHARD'
	elif n >= 7:
		return 'RICHARD'
	elif (n > 2) and (n - 1) > length or (n - 1) > width:
		return 'RICHARD'
	else:
		return 'GABRIEL'

def main():
	case_num = int(input())

	for case in range(case_num):
		n, length, width = tuple(map(int, input().split(' ')))
		result = compute(n, length, width)
		print("Case #", case+1, ": ", result, sep='')

if __name__ == "__main__":
    main()

