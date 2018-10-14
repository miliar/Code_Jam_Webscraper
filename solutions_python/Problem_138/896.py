#l1 = [0.186, 0.389, 0.907 , 0.832, 0.959, 0.557, 0.300, 0.992, 0.899]
#l2 = [0.916, 0.728, 0.271, 0.520, 0.700, 0.521, 0.215, 0.341,0.458]

#l1 = [0.5,0.1,0.9]
#l2 = [0.6,0.4,0.3]

def fairWar( l1,l2 ):
	l1.sort()
	l2.sort()
	points = 0
	n = len(l1)
	if n == 1:
		if l1[0] > l2[0]:
			points = points + 1
		return points
	else:
		i = 0
		while i < len(l2):
			if l2[i] > l1[0]:
				l2.pop(i)
				l1.pop(0)
			else:
				points = points + 1
				i += 1
		return points

#l3 = [0.7, 0.2]
#l4 = [0.8 ,0.3]

def getNum(l1,l2):
	l1.sort()
	l2.sort()
	m = l2[0]
	if len(l1) > 1:
		for i in range(len(l1)):
			if l1[i] > m:
				return i
				break
	return False
	
#l3 = [0.2,0.7]
#l4 = [0.8,0.9]
#l4 = [0.3,0.8]

def final2(l1,l2,points):
	i= 0
	if max(l1) < max(l2):
#		while i < len(l2):
		if l1[0] < l2[-1]:
			l2.pop()
			l1.pop(0)
#			print "hello\n" 
		else:
#			print "hi\n" 
			points = points + 1
			i += 1
#	print l1
#	print l2
	return points 

def final3(l1,l2,points):
	i = 0
	if max(l1) > max(l2):
		i = 0
#		while i < len(l2):
		points = points + 1
		l1.pop(getNum(l1,l2))
#		print "points: ", points
		l2.pop(0)
	return points
	

def deceitWar(l1,l2):
	l1.sort()
	l2.sort()
	points = 0
	k = 0
	n = len(l1)
	if n == 1:
		if l1[0] > l2[0]:
			points = points + 1
		return points
	else:
		while(len(l1) != 0):
			k = final2(l1,l2,k)
			if(len(l2) == 0):
				break
			k =	final3(l1,l2,k)
		return k
'''	else:
#		if max(l1) < max(l2):
#			while l1[0] < l2[-1]:
#				l1.pop(0)
#				l2.pop()
#			points = points + len(l1)
#			return points
			i = 0
			while i < len(l2):
				if l1[0] < l2[-1]:
					l2.pop()
					l1.pop(0)
				else:
					points = points + 1
					i += 1
			return points 
		else:
			i = 0
			while i < len(l2):
				points = points + 1
				l1.pop(getNum(l1,l2))
				l2.pop(0)
			return points - 1'''
	
#l3 = [0.186, 0.389, 0.907 , 0.832, 0.959, 0.557, 0.300, 0.992, 0.899]
#l4 = [0.916, 0.728, 0.271, 0.520, 0.700, 0.521, 0.215, 0.341,0.458]		

input_file = open("D-large.in","r");
output_file = open("D-large-attempt1.out","a");
m = input_file.readline()
#m = input()
for i in range(int(m)):
#	int1 = int(raw_input())
	int1 = input_file.readline();
#	k = raw_input()
	k = input_file.readline();
	l1 = [float(j) for j in k.split()]
#	k2 = raw_input()
	k2 = input_file.readline();
	l2 = [float(j) for j in k2.split()]
	l3 = [m for m in l1]
	l4 = [j for j in l2]
#	print "Case #" + str(i+1) + ": " + str(deceitWar(l1,l2)) + " " + str(fairWar(l3,l4))
	output_file.write("Case #" + str(i+1) + ": " + str(deceitWar(l1,l2)) + " " + str(fairWar(l3,l4)))
	output_file.write('\n')
