case = int(raw_input())
for j in range(case):
	first_answer = int(raw_input())
	a = []
	for i in range(4):
		a.append(map(int,raw_input().split()))

	second_answer = int(raw_input())
	b = []
	for i in range(4):
		b.append(map(int,raw_input().split()))

	final = list(set(a[first_answer-1])&set(b[second_answer-1]))
	if len(final) == 0:
		print "Case #%d: Volunteer cheated!"%(j+1)
	if len(final) == 1:
		print "Case #%d: %d"%(j+1,final[0])
	if len(final) > 1:
		print "Case #%d: Bad magician!"%(j+1)