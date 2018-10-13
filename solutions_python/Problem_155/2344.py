def game():
	T=input()
	loop=1
	ul=[]
	while loop<=T:
		ans1=raw_input()
        	list1=ans1.split(" ")
        	del list1[0]
        	ans=list(list1[0])
        	stood=0
        	need=0
        	for i in range(len(ans)):
			if stood>=i:
                		stood=stood+int(ans[i])
            		else:
                		need=need+1
				stood=stood+1+int(ans[i])
        	ul=ul+["Case #%s:"%loop+" %s"%need]
		loop=loop+1
	for i in ul:
        	print i
game()




			
