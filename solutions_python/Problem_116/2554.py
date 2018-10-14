#!/usr/bin/python


inputs=open('A-large.in','rd')
outputs=open('A.out','w')
case=(int)(inputs.readline())
for q in range(case):
	line1=inputs.readline()
	line2=inputs.readline()
	line3=inputs.readline()
	line4=inputs.readline()
	complete=1
	for c in line1:
		if ord(c)==46:
			complete=0
	for c in line2:
		if ord(c)==46:
			complete=0
	for c in line3:
		if ord(c)==46:
			complete=0
	for c in line4:
		if ord(c)==46:
			complete=0
	sumn=[]
	sumn.append(sum(ord(l) for l in line1)-10)
	sumn.append(sum(ord(l) for l in line2)-10)
	sumn.append(sum(ord(l) for l in line3)-10)
	sumn.append(sum(ord(l) for l in line4)-10)
	sumn.append(ord(line1[0])+ord(line2[0])+ord(line3[0])+ord(line4[0]))
	sumn.append(ord(line1[1])+ord(line2[1])+ord(line3[1])+ord(line4[1]))
	sumn.append(ord(line1[2])+ord(line2[2])+ord(line3[2])+ord(line4[2]))
	sumn.append(ord(line1[3])+ord(line2[3])+ord(line3[3])+ord(line4[3]))
	sumn.append(ord(line1[0])+ord(line2[1])+ord(line3[2])+ord(line4[3]))
	sumn.append(ord(line1[3])+ord(line2[2])+ord(line3[1])+ord(line4[0]))
	
	flag=0
	for j in sumn:
		if j==348 or j==352:
			outputs.write('Case #%d: X won\n' % (q+1))
			flag=1
			break
		elif j==321 or j==316:
			outputs.write('Case #%d: O won\n' % (q+1))
			flag=1
			break
	if flag==0:
		if complete==0:
			outputs.write('Case #%d: Game has not completed\n' % (q+1))
		else:
			outputs.write('Case #%d: Draw\n' % (q+1))
	inputs.readline()
inputs.close()
outputs.close()
