import string,os
f = open("trust.txt","r")
s = f.readlines()
f.close()
ret=""
for casen in range(1,int(s[0])+1):
	a=[]
	stp=[]
	for i in string.split(s[casen])[1:]:
	    if i.isalpha():
	        stp=[i]
	    else:
	        stp.append(int(i))
	        a.append(tuple(stp))
	#print a
	steps=0
	n=0
	opos=1
	bpos=1
	r=0
	
	def getNext(color):
	    for i in range(n,len(a)):
	        if a[i][0]==color:
	            return i
	    return -1
	
	while n<len(a):
	    #print n,steps,opos,bpos
	    steps+=1
	    if opos<a[getNext("O")][1]:
	        opos+=1
	        #print steps,"o+",opos
	    elif opos>a[getNext("O")][1]:
	        opos-=1
	        #print steps,"o-",opos
	    else:
	        if n==getNext("O"):
	            n+=1
	            r=1
	            #print steps,"o#",opos
	    if bpos<a[getNext("B")][1]:
	        bpos+=1
	        #print steps,"b+",bpos
	    elif bpos>a[getNext("B")][1]:
	        bpos-=1
	        #print steps,"b-",bpos
	    else:
	        if n==getNext("B") and r==0:
	            n+=1
	            #print steps,"b#",bpos
	    r=0
	
	print "Case #"+str(casen)+": "+str(steps)
	ret+="Case #"+str(casen)+": "+str(steps)+"\n"
f=open("return.txt","w")
f.write(ret)
f.close()
