""" codejam1 - To solve the magic trick 
Author: S.Satish
Purpose: To help the magician find out what number the volunteer chose
Usage : RUn the program it prints the output "Number, Bad Magician!, Volunteer Cheated!"""

# returns the magicians output.
# fixed natrix size 4 * 4

def magician(fdesc):
	matrix = []
	for i in range(4):
		k = [int(i) for i in fdesc.readline().strip().split(' ')]
		matrix.append(k)
	return matrix


# test cases
fdesc = open('A-small-attempt1.in','r')
fwrite = open('A-small-attempt.out','a')
t = fdesc.readline()
case = 0
for each in range(int(t)):
	q1 = (int(fdesc.readline())-1)
	arrangement1 = magician(fdesc)
	q2 = (int(fdesc.readline())-1)
	arrangement2 = magician(fdesc)
	x = arrangement1[q1]
	y = arrangement2[q2]
	e = []
	for f in x:
		if f in y:
			e.append(f)
	case += 1		
	if len(e) == 0:
		fwrite.write("Case #%d: Volunteer cheated!\n" %case)
	elif len(e) == 1:
		fwrite.write("Case #%d: %d\n" %(case, e[0]))
	elif len(e) > 1:
		fwrite.write("Case #%d: Bad magician!\n"%case)
fdesc.close()
fwrite.close()		 		
