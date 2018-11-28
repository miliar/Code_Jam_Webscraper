import sys

cases = int(sys.stdin.readline())
for i in range(0, cases):
	line = sys.stdin.readline().split(" ")
	N = int(line[0])
	S = int(line[1])
	p = int(line[2])
	answer = 0
	threshold = p*3 - 2
	
	for j in range(3, N+3):
		sc = int(line[j])
		if sc >= threshold:
			answer += 1
		elif sc >= threshold - 2:
			if S > 0 and sc > 1:
				S -= 1
				answer += 1
	
	print "Case #" + str(i+1) + ": " + str(answer)