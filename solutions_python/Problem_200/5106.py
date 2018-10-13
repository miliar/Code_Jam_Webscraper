dum=[]
def tidy(a):
	for i in range(len(a)-1):
		if int(a[i]) > int(a[i+1]):
			return False
	
	result.append(a)
	return True

num_ip=int(raw_input())
result=[]
for i in xrange(0,num_ip):
	val = int(raw_input())
	while val!=0:
		bol = tidy(str(val))
		if bol == False:
			val -= 1
		else:
			break

j=1
for i in result:
        print "Case #{}: {} ".format(j,i)
	j = j+1
