from sys import stdin
#import math

def find_next(list, color):
	try:
		return [y[0] for y in list].index(color)
	except:
		return -1
		
def move(current, goal):
	if current > goal:
		return -1
	elif current < goal:
		return 1
	else:
		return 0
		

f = open('outputA.txt', 'w')		
case = 1		
firstLine = True
for rad in stdin:
	if firstLine:
		firstLine = False
	else:
		rad = rad.split()
		list = []
		for i in range(0,int(rad[0])):
			#print rad[i*2+1],rad[i*2+2]
			list.append((rad[i*2+1], rad[i*2+2]))
		o_current = 1
		b_current = int(1)
		total = 0
		while list:
			o_next_butt = int(list[find_next(list,"O")][1])
			b_next_butt = int(list[find_next(list,"B")][1])
			#print o_next_butt,b_next_butt, find_next(list,"O"), find_next(list,"B")
			current = list.pop(0)
			#print "in", o_next_butt,o_current, "pow", b_next_butt, b_current, total 
			if current[0] == "O":
				while o_current != o_next_butt:
					o_current += move(o_current, o_next_butt)
					b_current += move(b_current, b_next_butt)
					total +=1
					#print "oo", o_next_butt,o_current, "lol", b_next_butt, b_current, total
				if o_current == o_next_butt:
					total+=1
					b_current += move(b_current, b_next_butt)
					#print "push"
			if current[0] == "B":
				while b_current != b_next_butt:
					o_current += move(o_current, o_next_butt)
					b_current += move(b_current, b_next_butt)
					total +=1
					#print "bb", o_next_butt,o_current, "lol", b_next_butt, b_current, total
				if b_current == b_next_butt:
					total +=1
					o_current += move(o_current, o_next_butt)
		f.write ( "Case #"+ str(case) + ": " + str(total) + "\n")
		case+=1	
					
					