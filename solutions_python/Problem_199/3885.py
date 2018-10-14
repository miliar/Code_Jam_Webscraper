# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.




def findMin(s, k):
	if s == "" or "-" not in s:
		return 0

	if len(s) < k:
		return -1

	if s[0] == "+":
		return findMin(trimmed(s), k)

	# print("s before flip: ", s)
	s = flip_first_k(s, k)
	# print("s after flip: ", s)
	result = findMin(trimmed(s), k)

	if result >= 0:
		return 1 + result
	else:
		return -1


def flip_first_k(s, k):

	result = "".join(["+" if char == "-" else "-" for char in s[:k]]) + s[k:]
	return result
 
def trimmed(s):
	i = 0
 	while i < len(s) and s[i] == "+":
 		i += 1
 	return s[i:]


t = int(raw_input())  # read a line with a single integer


for i in xrange(1, t + 1):
  s, k = [x for x in raw_input().split(" ")]  # read a list of integers, 2 in this case
  k = int(k)

  result = findMin(s, k)
  print "Case #{}: {}".format(i, result if result >= 0 else "IMPOSSIBLE")
