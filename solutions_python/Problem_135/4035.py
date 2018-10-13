import sys


def get_answer(CARD1,CARD2,rows1,rows2):
	caseA = set(rows1[CARD1-1])
	caseB =  set(rows2[CARD2-1])
	set_case = caseA & caseB
	set_case = list(set_case)
	if len(set_case) == 1:
		return int(set_case[0])
	elif len(set_case) < 1:
		return 'Volunteer cheated!'
	else:
		return 'Bad magician!'

file = open(sys.argv[1],'r')
f = [item.strip('\n') for item in file.readlines()]
file.close()

file = open(sys.argv[2],'w')
T = int(f[0])
index = 1
count = 1
while count <= T:
	CARD1 = int(f[index])
	rows1 = [f[index+1].split(' '),f[index+2].split(' '),f[index+3].split(' '),f[index+4].split(' ')]
	CARD2 = int(f[index+5])
	rows2 = [f[index+6].split(' '),f[index+7].split(' '),f[index+8].split(' '),f[index+9].split(' ')]
	returned_ans = get_answer(CARD1,CARD2,rows1,rows2)
	ans = 'Case #'+str(count)+': '+ str(returned_ans)
	file.write(ans)
	file.write('\n')
	index += 10
	count += 1
