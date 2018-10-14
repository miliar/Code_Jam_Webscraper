#read file
f = open('input.in', 'r')
lines = f.readlines()
f.close()
t = int(lines[0].split()[0])
total_lines = t*10 +1
opf = open('task.out', 'w')
for l in range(t):
	
	ch1 = int(lines[l*10+1].strip())
	ch2 = int(lines[l*10+6].strip())
	#char arays
	posb_nos= lines[l*10+ch1+1].split()
	selected_line = lines[l*10+ch2+6].split()
	#opf.write(str(l*10+ch1+1)+',')
	#opf.write(str(l*10+ch2+6))
	count=0;
	for no in posb_nos:
		if no in selected_line:
			capture_no=no
			count= count +1
	#opf.write('posb_nos: '+str(posb_nos))
	#opf.write('selected_line: '+str(selected_line))
	if count == 1:
		#print 'Case #'+l+1+': ',capture_no
		opf.write('Case #'+str(l+1)+': '+str(capture_no)+'\n')
	elif count >1 :
		opf.write('Case #'+str(l+1)+': Bad magician!\n')
	else :
		opf.write('Case #'+str(l+1)+': Volunteer cheated!\n')

opf.close()