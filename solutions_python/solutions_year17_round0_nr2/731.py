
input = open("B-large.in", "r")
output = open("B-large.out", "w")


T = int(input.readline().strip())

for j in range(1, T+1):
    output.write("case #{}: ".format(j))
    num = int(input.readline().strip())
    digits = [int(k) for k in str(num)]
    i = len(digits) - 1
    while True:
		if i == 0:
			break
		if digits[i] < digits[i - 1]:
			if digits[i - 1] == 1 and i == 1:
				digits.pop()
				digits[0] = 9
			else:
				digits[i - 1] -= 1
			for k in range(i, len(digits)):
				digits[k] = 9
		i = i - 1
    output.write("".join([str(k) for k in digits]))
    output.write("\n")


input.close()
output.close()

