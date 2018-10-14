import sys

for i in range(0, int(sys.stdin.readline())):
	n = list(sys.stdin.readline()[:-1])
	
	while True:
		modified = False
		digit = 0
		while digit < len(n) - 1:
			while int(n[0]) == 0:
				digit -= 1
				if digit < 0:
					digit = 0
				del n[0]
			
			if len(n) == 1:
				break
			
			if int(n[digit]) > int(n[digit + 1]):
				modified = True
				if int(n[digit]) == 0:
					n[digit + 1] = "9"
					
					idigit = digit
					while idigit >= 0:
						if int(n[idigit]) > 0:
							n[idigit] = str(int(n[digit]) - 1)
							break
						else:
							n[idigit] = "9"
						idigit -= 1
				else:
					n[digit] = str(int(n[digit]) - 1)
					n[digit + 1] = "9"
					
					x = 2
					while digit + x < len(n):
						n[digit + x] = "9"
						x += 1
			
			digit += 1
		
		if not modified:
			break
	print("Case #" + str(i + 1) + ": " + ''.join(n))
