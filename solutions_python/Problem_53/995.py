#snapper 
# google code jam 2010
# Bharadwaj
# 7 May 2010

f = open('A-small.in', 'r')
lines = f.readlines()
num = int(lines[0])
f.close()
f = open('small.out', 'w+')

inp = []
i = 1 # starting from 2nd line

while i <= num:
	line_at_i = lines [i]
	two_values = line_at_i.split()
	switches  = int(two_values[0])
	snaps = int(two_values[1])
	j,k = 0,0 #counter for swicthes,snaps
	#print switches, snaps
	while j < switches:
		inp.append(0)
		j = j + 1
	#print inp
	#start snapping
	zeropos = 0
	while k < snaps:
		#print "Snap " , k+1
		try:
			zeropos = inp.index(0)
		except ValueError:
			zeropos = len(inp) - 1
		inp = [(x + 1)%2 for x in inp[:zeropos + 1]] + inp[zeropos + 1:] #smart toggle :)
		#print inp
		k = k + 1
	onOff = 'OFF'
	try:
		k = inp.index(0) #reuse k
	except:
		onOff = 'ON'
	else:
		onOff = 'OFF'	
	toprint  = "Case #" + str(i) + ": " + onOff + "\n"
	f.write(toprint)
	i = i + 1
	inp[:] = []

f.close()