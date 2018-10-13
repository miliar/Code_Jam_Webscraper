def qui_gagne(a,b,c):
	if a == '1':
		return 'GABRIEL'
	elif a == '2':
		if int(b)*int(c)%2 == 0:
			return 'GABRIEL'
		else:
			return 'RICHARD'
	elif a == '3':
		if int(b)*int(c)%3 != 0:
			return 'RICHARD'
		elif int(b) == 1 or int(c) == 1:
			return 'RICHARD'
		else:
			return 'GABRIEL'
	else :
		if int(b)*int(c)%4 != 0:
			return 'RICHARD'
		elif int(b) <= 2 or int(c) <= 2:
			return 'RICHARD'
		else:
			return 'GABRIEL'

def solution_jam3():
	source = open("D:/Download/test.txt","r")
	output = open("D:/Download/jam3small.txt","w")
	liste = source.readline()
	liste = liste.split('\n')
	for i in range(int(liste[0])):
		liste = source.readline()
		liste = liste.split()
		output.write('Case #'+str(i+1)+': '+ qui_gagne(liste[0],liste[1],liste[2])+'\n')
	output.close()
	source.close()

solution_jam3()