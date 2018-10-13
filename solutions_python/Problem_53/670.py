f = open('input.txt', 'r')
amount = f.readline()
amount = int(amount)
i = 0
string = ''
for i in range(amount):
	# n amount of snapers
	# k total snaps
	
	temp = f.readline().partition(' ')
	n = int(temp[0])
	k = int(temp[2])
	k = k
	reg = k
	k = (k)%(pow(2,n))
	k = k+1
	inc = pow(2,n)
	sub = "OFF";
	if k == inc:
		sub = "ON";
	string+="Case #" + str(i+1) + ": "+sub+"\n"
	print "Case #" + str(i+1) + ": "+sub+" k: " + str(reg)

f = open('out.txt', 'w')
f.write(string)
