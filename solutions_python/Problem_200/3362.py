INPUT = "numbers.in"
OUTPUT = "numbers.out"

def check_range(digits, start, stop):
	for i in range(start, stop):
		if digits[i] < digits[i + 1]:
			return False
	return True

def replace_range(digits, value, start, stop):
	for i in range(start, stop+1):
		digits[i] = value

def solve(N):
	digits = list(str(N))
	digits = [int(x) for x in digits]
	digits.reverse()
	L = len(digits)
	for i in range(1, L):
		if digits[i] > digits[i - 1]:
			digits[i] -= 1
			replace_range(digits, 9, 0, i-1)
	digits.reverse()
	answer = int(''.join(map(str, digits)))
	return answer


def main(input_path, output_path):
	input_file = open(input_path, 'r')
	output_file = open(output_path, 'w')
	T = input_file.readline()
	T = int(T)
	for t in range(1, T + 1):
		N = input_file.readline()
		N = int(N)
		answer = solve(N)
		output_file.write("Case #{}: {}\n".format(str(t), str(answer)))


main(INPUT, OUTPUT)