#####################
#  Autor: alvarovmz@gmail.com
#####################

import sys
import re

#------------
#  Main
#------------
def main():

	try:
		test = open (sys.argv[1], 'r')
	except Exception:
		sys.exit(1)

	data = re.compile('^(\d+) (\d+)$')

	cases=[]

	for i in test.readlines():
		if data.match(i):
			cases.append(data.match(i).groups())

	run(cases)


#------------
#  Run
#------------
def run(cases):
	case = 1
	for i in cases:

		snappers=[]
		for j in range(0,(int)(i[0])):
			snappers.append(0)
		for k in range(0,(int)(i[1])):
			now=0
			power=1
			while (power and now < len(snappers)):
				if snappers[now]==0:
					power=0
				snappers[now]=(snappers[now]+1)%2
				now+=1
		print "Case #" + (str)(case)+":",
		bulb = 1
		for i in snappers:
			if i==0:
				bulb=0
				break
		if bulb==1:
			print "ON"
		else:
			print "OFF"

		case += 1

if __name__ == "__main__":
	if len(sys.argv)!=2:
		sys.exit(1)
	main()
