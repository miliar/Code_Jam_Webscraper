##################################
##	solve the war problem		##
##	the logic is that if min	##
##	value in Namoi's list is 	##
##	greater than the min value	##
## 	in Ken's list then remove	##
##	the two and give one point	##
## 	to Naomi. Else remove the	##
##	min from Namoi's list and 	##
##	max from Ken's list and		##
##	give 1 point to Ken			##
##	in case they are equal		##
##	no points given to each		##
##################################

import sys

def readData(f):
	data = []
	inputs = f.readline()
	count = 0
	rec = []
	for line in f:
		line = line.rstrip('\n\r\t')
		count = count + 1
		if count == 1:
			l = int(line)
			rec.append(l)
		else:
			temp = []
			for val in line.split():
				temp.append(float(val))
			rec.append(temp)
		if count == 3:
			count = 0
			data.append(rec)
			rec = []
	return data	

def war(naomi, ken):
	cntN=len(naomi)
	naomi.sort(reverse = True)
	ken.sort()
	for val in naomi:
		for kval in ken:
			if val < kval:
				cntN = cntN -1
				ken.remove(kval)
				break
	return cntN
			
	
def dwar(naomi, ken):
	cntN = 0
	cntK = 0
	lN = len(naomi)
	lK = len(ken)
	naomi.sort()
	ken.sort(reverse = True)
	while lN !=0:
		if naomi[lN-1]> ken[0]:
			cntN = cntN + 1
			del ken[0]
			lK = lK - 1
			del naomi[lN -1]
			lN = lN - 1
		elif naomi[0] < ken[lK-1]:
			cntK = cntK + 1
			del ken[0]
			lK = lK - 1
			del naomi[0]
			lN = lN - 1
		elif naomi[0] > ken[lK-1]:
			cntN = cntN + 1
			del ken[lK-1]
			lK = lK - 1
			del naomi[0]
			lN = lN - 1		
		elif naomi[0] == ken[lK -1]:
			del ken[lK-1]
			lK = lK - 1
			del naomi[0]
			lN = lN - 1
	return cntN
		
	
	
def main():
	"""main function
	./war.py filename"""
	if len(sys.argv)!= 2:
		print 'usage: %run war.py filename'
		sys.exit(1)
	f = open(sys.argv[1], 'r')
	data = readData(f)
	f.close()
	f = open('warout.txt','w')
	count = 1
	for rec in data:
		out='Case #'+str(count)+': '+str(dwar(rec[1][:], rec[2][:]))+' '+str(war(rec[1][:], rec[2][:]))
		print out
		f.write(out+'\n')
		count = count + 1
	f.close()
	
	
#call the main program
if __name__ == '__main__':
	main()