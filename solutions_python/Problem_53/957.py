import sys;
def main():
	filename = sys.argv[1]
	f=open(filename,'r')
	outf=open("output.txt", 'w')
	tcCount=int(f.readline())	
	
	# read test cases
	for i in range(tcCount):
		#print "Test case: ",(i+1)
		tc = str.split(f.readline())
		scnt = int(tc[0])
		snaps = int(tc[1])
		state = range(scnt)
		active = range(scnt)
		state =map(lambda x: 0, state)
		active=map(lambda x: 0, active)
		active[scnt-1]=1 # set last one to be active always
		
		k = 1
		while k <= snaps:
			for j in range(scnt):
				prevs = state[scnt-j-1]
				preva = active[scnt-j-1]
				state[scnt-j-1] = prevs ^ preva
				active[scnt-j-1] = 1 if scnt-j-1 == scnt-1 else state[scnt-j] & active[scnt-j]
			#print state,active	
			k = k+1	
		ans = state[0]&active[0]
		outline = 'Case #'+str(i+1)+': '+("ON" if ans==1 else "OFF")
		print outline
		outf.write(outline+'\n');
		
	f.close()
	outf.close()

			
main()

