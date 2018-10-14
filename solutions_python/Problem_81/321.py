import sys;
# Takes in a list and returns all possible permutations of the list
def getWP(l, ignorepos):
	win = 0
	played = 0
	for i in range(len(l)):
		if ignorepos > -1 and ignorepos == i:
			continue
		if l[i] == '1':
			win = win+1
		if l[i] != '.':
			played = played + 1
	return win/played
	
def getOWP(m,team):
	sum = 0
	for i in range(len(m)):
		if i != team and m[i][team] != '.':
			res = getWP(m[i],team)
			#print('getting res',res)
			sum = sum + res
	opp = 0		
	for i in range(len(m[team])):
		if m[team][i] != '.':
			opp = opp+1
	#print('getting sum,opp',sum,opp)
	
	return sum / opp
		
def getOOWP(owp, l):
	sum = 0
	cnt = 0
	for i in range(len(l)):
		if l[i] != '.':
			sum = sum + owp[i]
			cnt = cnt +1
	return sum/cnt
	
def main():
	filename = sys.argv[1]
	f=open(filename,'r')
	outf=open("output.txt", 'w')
	numtests = int(f.readline())
	total = numtests
	while numtests > 0:
		numtests = numtests - 1
		teamcnt=int(f.readline())
		matrix = []
		i=0
		wpm = []
		while i < teamcnt:
			line = f.readline()
			x = []
			for j in range(len(line)-1):
				x.append(line[j])
			matrix.append(x)
			i = i+1
		i=0
		owpm = []
		while i < teamcnt:
			team = matrix[i]
			wp = getWP(team, -1)
			owp = getOWP(matrix,i)
			#print ('wp',wp)
			#print ('owp',owp)
			wpm.append(wp)
			owpm.append(owp)
			i = i+1
		i=0
		outf.write('Case #'+str(total-numtests)+': \n')	
		while i < teamcnt:
			avg = getOOWP(owpm,matrix[i])
			#print ('oowp',avg)
			rpi = 0.25*wpm[i]+0.5*owpm[i]+0.25*avg
			outf.write(str(rpi)+'\n')	
			print ('rpi: ',rpi)
			i = i+1
			
		#print (matrix)
		# Matrix is stored
		
		
		
	f.close()
	outf.close()

main()
	
		