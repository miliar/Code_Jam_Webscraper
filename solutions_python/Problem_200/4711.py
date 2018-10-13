f=open('B-small-attempt0.in','r')
out=open('output.txt', 'w+')
c=0
u=1
lis=[]
for line in f:
    #print line
    ct = 0
    if c==0:
        tc = int(line)
        c=c+1
        continue
    else:
    	bh = ""
    	inp = int(line)
    	while inp > 0:
    		count = 1
    		i = inp
    		num = list(str(i))
    		#print "num", num
    		for j in range(len(num)):
    			#print "length and num:", range(len(num)), num
    			if j == 0:
    				continue
    			else:
    				#print "j", j
    				if int(num[j-1]) > int(num[j]):
    					#print ("test")
    					break
    				else:
    					count = count + 1 
    					#print "count", count
    				#print "count", count
    		if count == len(num):
    			for m in num:
    				bh = bh + str(m)
    			bh = bh + "\n"
        		j = "Case #{}: {}".format(u, bh)
        		out.write(j)
        		u+=1
    			break
    		inp = inp -1
f.close()
out.close()

    			