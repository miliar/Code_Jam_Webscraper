# n = input("Give me a fucking number: ")

# # num = int(n)

def start(num, ori):

	reversed = num[::-1]
	arr = []
	for d in str(reversed):
		arr.append(d)

	return tidy(arr, ori)


def tidy(arr, ori):
	for i in range(0, len(ori)-1):
		if int(arr[i]) < int(arr[i+1]):
			arr[i] = str(9)
			if int(''.join(arr)[::-1]) > int(ori):
				arr[i+1] = str(int(arr[i+1]) - 1)
			tidy(arr, ori)
			break

	return arr

file = open("B-large.in", "r")
file_out = open("output.txt", "w")
input = tuple(file)

for i in range(1, int(input[0])+1):
	
	num = input[i].replace("\n", "")
	answer = (''.join(start(num, num))[::-1]) + "\n"
	if answer[0] == '0':
		answer = answer[1:]
	file_out.write("Case #" + str(i) + ": " + answer)

