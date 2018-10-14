
import sys

def readInput(filePath):
	data = { 'nCase' : 0, 'cases' : [] }
	f = open(filePath, 'r')
	data['nCase'] = int(f.readline())
	for i in range(0, data['nCase']):
		answer1 = int(f.readline())
		arrange1 = []
		for j in range(4):
			arrange1.append(map(lambda x: int(x), f.readline().split(' ')))
		answer2 = int(f.readline())
		arrange2 = []
		for j in range(4):
			arrange2.append(map(lambda x: int(x), f.readline().split(' ')))
		data['cases'].append({
				'answer1' : answer1,
				'arrange1' : arrange1,
				'answer2' : answer2,
				'arrange2' : arrange2
				})

	return data

def getAnswer(case):
	expect1 = case['arrange1'][case['answer1'] - 1]
	expect2 = case['arrange2'][case['answer2'] - 1]
	answers = []
	for val1 in expect1:
		for val2 in expect2:
			if val1 == val2:
				answers.append(val1)
	
	return answers


def main(argv):
	if len(argv) != 3:
		print 'Usage: main <input_file> <output_file>'
		return

	data = readInput(argv[1])
	output = open(argv[2], 'w')
	for idx, val in enumerate(data['cases']):
		answers = getAnswer(val)
		if (len(answers) == 1):
			output.write('Case #%d: %d\n' % (idx + 1, answers[0]))
		elif (len(answers) > 1):
			output.write('Case #%d: %s\n' % (idx + 1, 'Bad magician!'))
		elif len(answers) == 0:
			output.write('Case #%d: %s\n' % (idx + 1, 'Volunteer cheated!'))

main(sys.argv)

