#!/usr/bin/python

def rotate_string(string, d):
	for i in range(0,d):
		string =  string[1:] + string[:1]
	return string

def is_inlist(l, value):
	try:
		l.index(value)
		return True
	except:
		return False




rawfile="C-small-attempt0.in"
#rawfile="A-large-practice.in"
ansfile="a"


hf=open(rawfile,'r')
hw=open(ansfile,'w')

line=hf.readline()
line=line.rstrip()
cases=int(line)

for idx in range(1,cases+1):
	line=hf.readline().rstrip()
	raw = line.split(' ')
	A = int(raw[0])
	B = int(raw[1])
	
	num=0
	pair=[]
	for i in range(A, B+1):
		rotatelist = []
		for n in range(1,len(str(i))):
			rotate =  rotate_string(str(i), n)
			if(i < int(rotate)):
				isalready = 0
				if(int(rotate) >= A and int(rotate) <= B):
					if(not is_inlist(rotatelist, int(rotate))):
						rotatelist.append(int(rotate))
						pair.append((i, int(rotate)))
		
						num+=1
	
	
	print "Case #" + str(idx) + ": " + str(num)
	hw.write("Case #" + str(idx) + ": " + str(num) + "\n")

#print "######################"
#for i in range(0,len(pair)):
#	print pair[i]
	
	#hw.write("Case #" + str(idx) + ": ")

	#for i in range(0,len(line)):
	#	hw.write(dict[line[i]])
	#hw.write("\n")
	

	
