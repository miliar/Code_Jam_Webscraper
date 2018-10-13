#magic.py - Python 3.2.1

from sys import argv

fin = open(argv[1])
fout = open(argv[1].replace(".in",".out"),'w')
T=int(fin.readline())
for Tt in range(1,T+1):

	r=int(fin.readline())
	for i in range(r-1): next(fin)
	row1=set(fin.readline().split())
	for i in range(4-r): next(fin)
	
	r=int(fin.readline())
	for i in range(r-1): next(fin)
	row2=set(fin.readline().split())
	for i in range(4-r): next(fin)
	
	r=row1&row2
	if(len(r)==0): s="Volunteer cheated!"
	elif(len(r)>1): s="Bad magician!"
	else: s=r.pop()
	fout.write('Case #{0}: {1}\n'.format(Tt,s))
	
fin.close()
fout.close()