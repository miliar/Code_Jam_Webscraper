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
		rounds = int(tc[0])
		capacity = int(tc[1])
		groupcnt = int(tc[2])
		groups = map(int,str.split(f.readline()))
		
		cost = 0
		k = 0
		while k < rounds:
			space = capacity
			queue = []
			while space <= capacity:
				if len(groups) <=0 or groups[0] > space:
					break
				ride = groups.pop(0)
				cost = cost +  ride
				queue.append(ride)
				space = space - ride
			groups.extend(queue)
			k = k+1	
		ans = cost
		outline = 'Case #'+str(i+1)+': '+str(cost)
		print outline
		outf.write(outline+'\n');
		
	f.close()
	outf.close()

			
main()

