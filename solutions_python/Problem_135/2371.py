#! /usr/bin/env python3.4

def solution(i, r1, grid1, r2, grid2):
	outfile = open("output.txt", "a")
	row1 = grid1[int(r1)-1]
	row2 = grid2[int(r2)-1]
	matches = set(row1).intersection(row2)
	ans = ""
	if len(matches) == 1:
		for e in matches:
			ans = e
			break
	elif len(matches) > 1:
		ans = "Bad magician!"
	else: 
		ans = "Volunteer cheated!"
	line = 'Case #{0}: {1} \n'.format(i+1, ans)
	outfile.write(line)
	
	return
# Start
file = open("A-small-attempt0.in")
T = file.readline()
for i in range(0, int(T)):
	r1 = file.readline()
	grid1 = []
	for row in range(0,4):
		grid1.append(file.readline().strip().split())
	r2 = file.readline() 
	grid2 = []
	for row in range(0,4):
		grid2.append(file.readline().strip().split())
	
	solution(i, r1, grid1, r2, grid2)

				