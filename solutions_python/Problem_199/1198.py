
def flip(char):
	if char == "+":
		return "-"
	else:
		return "+"

def flip_all(string):
	return ''.join(list(map(flip,string)))


def flip_k(string, k, index):
	if len(string) >= index + k:
		return (string[:index] + flip_all(string[index:index+k]) + string[index+k:])
	else:
		return string

def flip_contiguous(string, k):
	index = 0
	count = 0
	while index + k <= len(string):
		if string[index] == "-":
			string = string[:index] + flip_all(string[index:index+k]) + string[index+k:]
			count += 1
		index += 1
	index = 0
	while index < len(string):
		if string[index] == "-":
			return "IMPOSSIBLE"
		index += 1
	return count

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  test_case = str(input())
  lst = test_case.split()
  print("Case #{}: {}".format(i, flip_contiguous(lst[0], int(lst[1]))))


#print (flip("+"))
#print (flip_all("+-+"))
#print (flip_k("+-+-+-+-+", 4, 0))
#print (flip_k("+-+-+-+-+", 4, 1))
#print (flip_k("+-+-+-+-+", 4, 2))
#print (flip_k("+-+-+-+-+", 4, 3))
#print (flip_k("+-+-+-+-+", 4, 4))
#print (flip_k("+-+-+-+-+", 4, 5))
#print (flip_k("+-+-+-+-+", 4, 6))
#print (flip_contiguous("---+-++-", 3))
#print (flip_contiguous("+++++", 4))
#print (flip_contiguous("-+-+-", 4))