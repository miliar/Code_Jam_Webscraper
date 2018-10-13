import sys

f = open(sys.argv[1], 'r')
lines = f.readlines()
lines.pop(0)
f.close()

f = open('asdf.txt', 'w')
c = 0
for l in lines:
	c += 1
	O_location = 1
	B_location = 1
	turns = []
	moves = {"O":[], "B":[]}
	l = l.split()
	for i in range(1, len(l), 2):
		moves[l[i]].append(int(l[i+1]))
		turns.append(l[i])
	answer = 0
	while turns:
		Omoved = 0
		Bmoved = 0
		answer += 1
		if moves['O'] and O_location < moves['O'][0]:
			O_location += 1
			Omoved = 1
		elif moves['O'] and O_location > moves['O'][0]:
			O_location -= 1
			Omoved = 1
		if moves['B'] and B_location < moves['B'][0]:
			B_location += 1
			Bmoved = 1
		elif moves['B'] and B_location > moves['B'][0]:
			B_location -= 1
			Bmoved = 1
		
		if moves['O'] and O_location == moves['O'][0] and turns[0] == 'O' and not Omoved:
			turns.pop(0)
			moves['O'].pop(0)
		elif moves['B'] and B_location == moves['B'][0] and turns[0] == 'B' and not Bmoved:
			turns.pop(0)
			moves['B'].pop(0)
	f.write("Case #" + str(c) + ": " + str(answer) + '\n')

f.close()