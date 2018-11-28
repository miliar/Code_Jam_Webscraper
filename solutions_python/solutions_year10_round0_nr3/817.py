#####################
#  Autor: alvarovmz@gmail.com
#####################

import sys
from collections import deque
#------------
#  Main
#------------
def main():

	try:
		test = open (sys.argv[1], 'r')
	except Exception:
		sys.exit(1)


	cases=[]

	for i in test.readlines():
		cases.append(i[:-1].split(' '))

	run(cases)


#------------
#  Run
#------------
def run(cases):

	tests=(int)(cases[0][0])
	cases=cases[1:]

	i = 0
	case=1
	while(case<=tests):
		roller=deque(cases[i+1])
		r=(int)(cases[i][0])
		capacity=(int)(cases[i][1])
		groups=(int)(cases[i][2])
		euros=0

		for j in range(0,r):
			people=0
			k=0
			while (k<groups and people+(int)(roller[0]) <= capacity):
				people += (int)(roller[0])
				roller.append(roller.popleft())
				k+=1
		#	print roller
			euros += people

		print "Case #" + (str)(case)+": "+(str)(euros)

		i+=2
		case += 1

if __name__ == "__main__":
	if len(sys.argv)!=2:
		sys.exit(1)
	main()
