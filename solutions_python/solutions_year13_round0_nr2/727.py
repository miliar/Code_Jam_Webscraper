f = open('B-large.in','r')
prompt = ''.join(f.readlines())
f.close()
#print prompt
p = prompt.split('\n')
count = 0
list_of_yards = []
while count < len(p):
	#print p[count]
	if count == 0:
		num_of_test_cases = int(p[count])
		count += 1
	print str(count) + ":" + str(int(p[count].split()[0]))
	dim = int(p[count].split()[0]),int(p[count].split()[1])
	cd = 0
	yard = []
	while cd < dim[0]:
		row = []
		cd += 1
		count += 1
		for a in p[count].split():
			row.append(int(a))
		yard.append(row)
	list_of_yards.append(yard)
	count += 1

#list of yards is now built

def is_yard_mowable(y):
	#check every position in the yard
	#for all y yard[pos_x][y] <= height or for all x yard[x][pos_y] <= height
	for pos_y in xrange(0,len(y)):
		for pos_x in xrange(0,len(y[pos_y])):
			#check vertical and horizantal
			h = y[pos_y][pos_x]
			can_horiz = True
			for a in xrange(0,len(y)):
				if y[a][pos_x] > h:
					can_horiz = False
					break
			can_vert = True
			for a in xrange(0,len(y[pos_y])):
				if y[pos_y][a] > h:
					can_vert = False
					break
			if not (can_vert or can_horiz):
				return 'NO'
	return 'YES'
count = 0
final_out = ""
for a in list_of_yards:
	count += 1
	final_out += "Case #" + str(count) + ": " + is_yard_mowable(a) + '\n'
f = open('output2.txt','w')
f.write(final_out)
f.close()