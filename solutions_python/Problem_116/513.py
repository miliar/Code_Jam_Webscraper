from threading import *
import sys


class Solver(Thread):

	def __init__(self, caseId, array, answer):
		Thread.__init__(self)
		self.caseId = caseId + 1
		self.array = array
		self.answer = answer

	def run(self):
		res = "Case #" + str(self.caseId) + ": "
		array = self.array
		notDone = False

		for i in range(4):
			tmp = 0
			isT = False
			for j in range(4):
				if array[i][j] == 'X':
					tmp -= 1
				elif array[i][j] == 'O':
					tmp += 1
				elif array[i][j] == 'T':
					isT = True
				else:
					notDone = True
					break
			if tmp == 4 or tmp == 3 and isT:
				res += "O won"
				self.answer[self.caseId] = res
				return
			if tmp == -4 or tmp == -3 and isT:
				res += "X won"
				self.answer[self.caseId] = res
				return

			tmp = 0
                        isT = False
                        for j in range(4):
                                if array[j][i] == 'X':
                                        tmp -= 1
                                elif array[j][i] == 'O':
                                        tmp += 1
                                elif array[j][i] == 'T':
                                        isT = True
                                else:
                                        notDone = True
                                        break
                        if tmp == 4 or tmp == 3 and isT:
                                res += "O won"
				self.answer[self.caseId] = res
				return
                        if tmp == -4 or tmp == -3 and isT:
                                res += "X won"
				self.answer[self.caseId] = res
				return

		tmp = 0
		isT = False	
		for i in range(4):	
			if array[i][i] == 'X':
	                        tmp -= 1
                        elif array[i][i] == 'O':
                                tmp += 1
                        elif array[i][i] == 'T':
                                isT = True
                        else:
                                notDone = True
                                break
                if tmp == 4 or tmp == 3 and isT:
                        res += "O won"
			self.answer[self.caseId] = res
			return
                if tmp == -4 or tmp == -3 and isT:
                        res += "X won"
			self.answer[self.caseId] = res
			return


		tmp = 0
                isT = False
                for i in range(4):
                        if array[i][3-i] == 'X':
                                tmp -= 1
                        elif array[i][3-i] == 'O':
                                tmp += 1
                        elif array[i][3-i] == 'T':
                                isT = True
                        else:
                                notDone = True
                                break
                if tmp == 4 or tmp == 3 and isT:
                        res += "O won"
			self.answer[self.caseId] = res
                        return
                if tmp == -4 or tmp == -3 and isT:
                        res += "X won"
			self.answer[self.caseId] = res
                        return

		if notDone:
			res += "Game has not completed"
			self.answer[self.caseId] = res
			return
		res += "Draw"
		self.answer[self.caseId] = res
		

def prepare():
	lines = sys.stdin.readlines()
	nbCase = int(lines[0])
	case = {}
	for i in range(nbCase):
		case[i] = []
		for l in range(4):
			case[i].append(lines[1+i*5+l])
	return case
if __name__ == "__main__":

	prep = prepare()
	answer = {}
	for i in prep:
		Solver(i, prep[i], answer).start()

	for i in answer:
		print answer[i]
