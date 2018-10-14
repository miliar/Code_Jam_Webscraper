f = open('A-small-attempt1.in.txt','r')
text_file = open("Output.txt", "w")
numberOfCase = int(f.readline())

storage = []
for x in xrange(0,numberOfCase):
	row = []
	firstanswer = int(f.readline())

	for k in xrange(0,4):
		y = f.readline()
		y = y.strip()
		z = y.split(' ')
		row.append(z)

	storage = row[firstanswer-1]
	secondanswer = int(f.readline())

	row = []
	for k in xrange(0,4):
		y = f.readline()
		y = y.strip()
		z = y.split(' ')
		row.append(z)

	count = 0
	for i in storage:
		if i in row[secondanswer-1]:

			answer = i;
			count+=1
	
	if count == 1:
		text_file.write("Case #"+str(x+1)+": "+answer+"\n")
	elif count == 0:
		text_file.write("Case #"+str(x+1)+": Volunteer cheated!"+"\n")
	else:
		text_file.write("Case #"+str(x+1)+": Bad magician!"+"\n")


text_file.close()




