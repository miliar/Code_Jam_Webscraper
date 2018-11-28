import sys
from collections import deque

	
def main():
	infile = open(sys.argv[1], 'r')
	outfile = open(sys.argv[1][:-2] + 'out', 'w')
	
	for case in range(1, int(infile.readline())+1):
		runsperday, capacity, groups = (int(number) for number in infile.readline().split())
		
		groups = deque([int(number) for number in infile.readline().split()])
		
		cash = 0
		
		for i in range(runsperday):
			full = False
			seated = 0
			gcnt = 0
			while not full:
				if (groups[0]+seated)>capacity or gcnt==len(groups):
					full = True	
				else:
					gcnt+=1
					group = groups[0]
					seated+=group
					groups.append(group)
					groups.popleft()
			cash+=seated
			if len(groups)==0:
				break
			
		outfile.write("Case #%i: %i\n" %(case, cash))
		

if __name__ == "__main__":
	main()