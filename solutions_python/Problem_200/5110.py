def thwart(word):
	word=str(word)
	counter=len(word)
	counter=counter-1
	spit=[]
	while counter>=0:
		spit.append(word[counter])
		counter=counter-1
	spit.reverse()
	return spit

def loop(hyper):
	num=[]
	for items in hyper:
		item=int(items)
		num.append(item)
	return num

def numer(numbers):
	condit=0
	length=(len(numbers)-1)
	while length>0:
		if numbers[length]>=numbers[(length-1)]:
			condit=condit+1
		length=length-1
	length=(len(numbers)-1)
	if condit==length:
		return 0
	else:
		return 1

def sheep(counter):
	counter_dup=1
	while counter_dup<=counter:
		num=input()
		boolean=1
		while boolean==1:	
			num_o=str(num)	
			num_new=thwart(num_o)
			num_new=loop(num_new)
			boolean=numer(num_new)
			num=num-1
		num=num+1
		print "Case #{}: {}".format(counter_dup,num)
		counter_dup=counter_dup+1
sheep(input())
