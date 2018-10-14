import sys
sys.stdin = open("inputs.in");
sys.stdout = open('outputs.out', 'w')
Answers = []
for t in range(int(input())):
	lstCards1, lstCards2 = set([]),set([]) 
	row = int(input())
	for i in range(1,5):
		if row == i:
			lstCards1 |= set(input().split())
		else:
			input()
	row = int(input())
	for i in range(1,5):
		if row == i:
			lstCards2 |= set(input().split())
		else:
			input()
	Answers.append([t+1, lstCards1 & lstCards2])
for case in Answers:
	if (len(case[1]) == 1):
		print ("Case #%d: %d"%(case[0], int(case[1].pop())))
	elif (len(case[1]) > 1):
		print ("Case #%d: Bad magician!"%case[0])
	else:
		print ("Case #%d: Volunteer cheated!"%case[0])