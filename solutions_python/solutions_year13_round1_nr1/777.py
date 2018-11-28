

tc=input()
casei=1

pi = 3.14159265359


while casei<=tc:
	count = 0
	line = raw_input()
	r=int(line.split(" ")[0])
	paint=int(line.split(" ")[1])
	#print r
	i=1
	go=1
	while(go==1):
		req =  ( pow((r+i),2) - pow((r+i-1),2))
		if(paint >=req):
			paint = paint - req
			count = count + 1
			i=i+2
			#print paint
		else:
			go=0	
	
	print "Case #"+str(casei)+": "+str(count)
	casei = casei+1
