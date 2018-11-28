# magictrick.py
#
# Nate Beatty
# http://natebeatty.com
# April 12, 2014
#
# Google Code Jam | Qualification Round
# Problem A. Magic Trick
#

# import sys

def toInt(array):
    return map(int, array)

def readInput():
	filePath = 'A-small-attempt0.in.txt'
	f = open(filePath)
	lines = [line.strip().split(' ') for line in f]
	lines = map(toInt, lines)
	f.close()
	return lines

def playGame(board1, board2):
	return list(set(board1[board1[0][0]]) & set(board2[board2[0][0]]))


txtinput = readInput()
rounds = txtinput[0][0]

for i in range(rounds):
	j = 1 + (i * 10)
	result = playGame(txtinput[j: j+5], txtinput[j+5:j+11]);
	y = 'Bad magician!'
	if (len(result) == 0): y = 'Volunteer cheated!'
	if (len(result) == 1): y = str(result[0])
	print 'Case #' + str(i + 1) + ': ' + y
