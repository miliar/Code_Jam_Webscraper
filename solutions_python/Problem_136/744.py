def cookieAlpha():
	for i in range(input()):
		RATE = 2
		COST, FARM, TARGET = [float(j) for j in raw_input().strip().split()]
		if TARGET < COST:
			print 'Case #%d: '%(i+1), "%.7f"%(TARGET/ RATE)
		else:
			TIME = COST/2
			while 1:
				if (TARGET - COST)/RATE < TARGET/(RATE+FARM):
					TIME = TIME + (TARGET - COST)/RATE
					break
				else:
					TIME = TIME + COST/(RATE+FARM)
					RATE = RATE + FARM
			print 'Case #%d: '%(i+1), "%.7f"%TIME
			
if __name__ == '__main__':
	cookieAlpha()
		
		
