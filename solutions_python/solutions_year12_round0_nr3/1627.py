def main():
	f = open('file.in','r')
	NumCases=int(f.readline())
	for i in range (1,NumCases+1):
		min,max=f.readline()[:-1].split(' ')
		Min=int(min)
		Max=int(max)
		count=0
		for j in range(Min,Max+1):
			L=[]	
			for k in range (1,len(str(j))):
				rotate=int(str(j)[k:len(str(j))]+str(j)[0:k])
				if rotate<=Max and rotate > j and rotate not in L :
					L.append(rotate)	
					#print j, rotate
					count+=1	
		print "Case #%s: %s" % (i,count)

if __name__ == '__main__': main()       

