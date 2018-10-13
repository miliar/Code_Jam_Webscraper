import math

def is_palindrome(string):
	l = len(string)

	if l == 1:
		return True

	if l % 2 == 0:
		return string[:l/2] == string[l/2:][::-1]

	return string[:l/2] == string[(l/2)+1:][::-1]


# Gets the number of square and palindrome numbers between a and b
def nbrs(a, b):
	count = 0
	for i in range(int(a), int(b)+1):
		if is_palindrome(str(i)):
			sq = math.sqrt(i)
			if sq % 1 == 0:
				sq = int(sq)
				if is_palindrome(str(sq)):
					count += 1

	return count

def main():
	f = open('/Users/alex/Downloads/C-small-attempt0.in.txt')
	nTests = int(f.readline().replace("\n",""))

	for i in range(nTests):
		line = f.readline().replace("\n","")
		numbers = line.split(" ")
		a = numbers[0]
		b = numbers[1]

		print "Case #" + str(i+1) + ": " + str(nbrs(a, b))


if __name__ == "__main__":
    main()