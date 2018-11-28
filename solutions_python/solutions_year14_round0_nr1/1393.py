# import sys
# import csv
# import os
# import re
# import datetime
# import datamerge

fin = open('A-small-attempt2.in','r')
fout = open('A-small-attempt-output.in','w')

lines = fin.read().splitlines()
N = int(lines[0])
# print N
for i in range(N):
	selected_row1 = int(lines[i*10+1])
	selected_row2 = int(lines[i*10+6])
	row1 = lines[(i)*10+selected_row1+1].split(' ')
	row2 = lines[(i)*10+selected_row2+6].split(' ')
	possible_cards = []
	for r in row1:
		if row2.count(r) > 0:
			possible_cards.append(r)
	# print possible_cards
	if (len(possible_cards)==1):
		str=  'Case #%d: %s\n'%(i+1,possible_cards[0])
	elif (len(possible_cards)>1):
		str = 'Case #%d: Bad magician!\n'%(i+1)
	else:
		str= 'Case #%d: Volunteer cheated!\n'%(i+1)
	fout.write(str)

fin.close()
fout.close()
