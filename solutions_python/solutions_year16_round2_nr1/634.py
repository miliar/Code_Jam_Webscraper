def main():
	f = open('A-large.in', 'r')
	t = int(f.readline())
	for i in range(t):
		s = f.readline().strip()
		number = phoneNumber(s)
		print('Case #' + str(i+1) + ': ' + ''.join([str(x) for x in number]))
	f.close()
	
def phoneNumber(s):
	digits = []
	alphabet = [0] * 26
	for c in s:
		alphabet[ord(c) - ord('A')] += 1
	
	while alphabet[ord('Z') - ord('A')]:
		digits.append(0)
		alphabet[ord('Z') - ord('A')] -= 1
		alphabet[ord('E') - ord('A')] -= 1
		alphabet[ord('R') - ord('A')] -= 1
		alphabet[ord('O') - ord('A')] -= 1
		
	while alphabet[ord('W') - ord('A')]:
		digits.append(2)
		alphabet[ord('T') - ord('A')] -= 1
		alphabet[ord('W') - ord('A')] -= 1
		alphabet[ord('O') - ord('A')] -= 1
		
	while alphabet[ord('X') - ord('A')]:
		digits.append(6)
		alphabet[ord('S') - ord('A')] -= 1
		alphabet[ord('I') - ord('A')] -= 1
		alphabet[ord('X') - ord('A')] -= 1
		
	while alphabet[ord('G') - ord('A')]:
		digits.append(8)
		alphabet[ord('E') - ord('A')] -= 1
		alphabet[ord('I') - ord('A')] -= 1
		alphabet[ord('G') - ord('A')] -= 1
		alphabet[ord('H') - ord('A')] -= 1
		alphabet[ord('T') - ord('A')] -= 1
		
	while alphabet[ord('H') - ord('A')]:
		digits.append(3)
		alphabet[ord('T') - ord('A')] -= 1
		alphabet[ord('H') - ord('A')] -= 1
		alphabet[ord('R') - ord('A')] -= 1
		alphabet[ord('E') - ord('A')] -= 2
		
	while alphabet[ord('S') - ord('A')]:
		digits.append(7)
		alphabet[ord('S') - ord('A')] -= 1
		alphabet[ord('V') - ord('A')] -= 1
		alphabet[ord('N') - ord('A')] -= 1
		alphabet[ord('E') - ord('A')] -= 2
		
	while alphabet[ord('V') - ord('A')]:
		digits.append(5)
		alphabet[ord('F') - ord('A')] -= 1
		alphabet[ord('I') - ord('A')] -= 1
		alphabet[ord('V') - ord('A')] -= 1
		alphabet[ord('E') - ord('A')] -= 1
		
	while alphabet[ord('F') - ord('A')]:
		digits.append(4)
		alphabet[ord('F') - ord('A')] -= 1
		alphabet[ord('O') - ord('A')] -= 1
		alphabet[ord('U') - ord('A')] -= 1
		alphabet[ord('R') - ord('A')] -= 1
		
	while alphabet[ord('I') - ord('A')]:
		digits.append(9)
		alphabet[ord('N') - ord('A')] -= 2
		alphabet[ord('I') - ord('A')] -= 1
		alphabet[ord('E') - ord('A')] -= 1
		
	digits += [1] * alphabet[ord('O') - ord('A')]
	return sorted(digits)



if __name__ == '__main__':
	main()
