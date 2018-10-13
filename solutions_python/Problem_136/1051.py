##################################
##	solve the cookie problem	##
##	the logic is to find at		##
##	every step if it is better 	##
##	to earn X cookies with the	##
##	current speed or to upgrade	##
##	speed and then earn X		##
##	cookies. The measure is time##
##	choose the option recursively##
##################################

import sys

def readData(f):
	data = []
	inputs = f.readline()
	print inputs
	for line in f:
		line = line.rstrip('\n\r\t')
		temp = []
		for val in line.split():
			temp.append(float(val))
		data.append(temp)
	return data	

def result(C,F,X):
	time = 0
	speed = 2.0
	time1 = 2
	time2 = 1
	while time1 > time2:
		time1 = X/speed
		upgradedSpeed = speed + F
		time2 = C/speed + X/upgradedSpeed
		if time1>time2:
			time = time + C/speed
			speed = upgradedSpeed
		else:
			time = time + time1
	return time
	
def main():
	"""main function
	./cookie.py filename"""
	if len(sys.argv)!= 2:
		print 'usage: %run cookie.py filename'
		sys.exit(1)
	f = open(sys.argv[1], 'r')
	data = readData(f)
	f.close()
	f = open('cookietout.txt','w')
	count = 1
	for rec in data:
		out='Case #'+str(count)+': '+str(result(rec[0],rec[1],rec[2]))
		print out
		f.write(out+'\n')
		count = count + 1
	f.close()
	
	
#call the main program
if __name__ == '__main__':
	main()