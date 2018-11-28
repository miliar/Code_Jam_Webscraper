








f = open('A-large.in', 'r')
test = int(f.readline())
#print test

for value in range(test):
	val = f.readline().split()
	need = 0
	total = 0
	for number in range(int(val[0])+1):
		#print "NUMERO: "+str(val[1][number])
		if int(val[1][number]) != 0 and total < number:
			#print "ME FALTAN: " + (str(number-total)),"NUMERO "+str(number),"TOTAL "+str(total)
			need += number-total
			total += number - total
		total += int(val[1][number])
	print "Case #"+str(int(value +1))+": "  +str(need)

