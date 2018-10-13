def read():
	return raw_input().split(" ")

def test_case():
	first_answer = int(raw_input())
	x = []
	for row in range(4):
		x.append(map(int,read()))
	options_a = x[first_answer-1]
	
	second_answer = int(raw_input())
	y = []
	for row in range(4):
		y.append(map(int,read()))
	options_b = y[second_answer-1]
	
	options = set(options_a).intersection(set(options_b))
	options = list(options)
	if len(options) == 1:
		return options[0]
	elif len(options) == 0:
		return "Volunteer cheated!"
	else:
		return "Bad magician!"
	

def main():
	test_cases = int(raw_input())
	for i in range(test_cases):
		res = test_case()
		print "Case #%d: %s" % (i+1, res)

if __name__ == "__main__":
	main()
