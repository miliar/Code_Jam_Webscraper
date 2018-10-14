import sys
max_trycount = 100

## input output part ----------------##
def read_input():
	input = {}
	with open(sys.argv[1],"r") as f:
		data = f.readlines()

	input["testcount"] = int(data.pop(0))
	tests =[]
	for line in data:
		n = line.strip()
		tests.append(int(n))
	
	input["tests"] = tests
	return input


def save_output(results):
	with open("output.txt", "w") as f:
		for result in results:
			print "Case: #{}: {}\n".format(result["case"],result["result"])
			f.write("Case #{}: {}\n".format(result["case"],result["result"]))

## end of input output part ----------------##
def in_order(number):
	numbers = [int(x) for x in str(number)]
	sorted_numbers = sorted(numbers)
	if numbers == sorted_numbers:
		return True
	else:
		return False

def run(input):
	results = []
	for case in range(1,input["testcount"]+1):
		results.append({"case":case, "result": test_cases(input["tests"][case-1])})

	return results

def test_cases(number):
	while True:
		number_digits = [int(x) for x in str(number)]
		for i in range(0,len(number_digits)-1):
			if number_digits[i+1] < number_digits[i]:
				print number_digits[i:]
				temp = int("".join([str(x) for x in number_digits[i+1:]]))
				number -= temp
				break

		if in_order(number):
			return number
		else:
			return test_cases(number-1)


if __name__ == "__main__":
	test_cases(10)
	input = read_input()
	print "input:", input
	results = run(input)
	#print "results:", results
	#results = [{"case":1, "result": 3},{"case":1, "result": 1},{"case":1, "result": "Impossible"}]
	save_output(results)



