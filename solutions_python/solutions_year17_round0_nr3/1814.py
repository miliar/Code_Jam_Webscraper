	
	

if __name__ == "__main__":

	t = int(raw_input())
	for i in range(1, t+1):
		n,k = [int(s) for s in raw_input().split(" ")]
		# n stalls (between 2 end stalls)

		#sl is a sparse list - 0 indicates occupied stall, 
		#integers indicate number of empty stall at a stretch
		spl = [0,n,0] #initial situation

		#same in text form to make new sparse list generation easier
		tspl = [str(x) for x in spl] 


		#when every person enters, (s)he effectively 
		#looks for the largest stretch of unoccupied stalls and 
		#picks the middle one in that stretch
		
		for person in range (0,k):
			pos = spl.index(max(spl)) #okay since leftmost picked in case of tie
			
			#need to change the sparse list at index pos 
			#it will become approx n/2 0 n/2
			#use string format sparse list to replace 
			#then resplit list to get ints for future iterations

			val = spl[pos]
			
			if val%2 == 1: #if odd, pick middle
			#	newstr = str((val-1)/2)+"0"+str((val-1)/2)
				ls = rs = (val-1)/2
			else:
			#	newstr = str(val/2-1)+"0"+str(val/2)
				ls = val/2 -1
				rs = val/2
			
			newstr = str(ls)+";0;"+str(rs)
			
			#replace in text form to make easier to split
			tspl[pos] = newstr
			
			tspl = (";").join(tspl).split(";")
			
			spl = [int(x) for x in tspl]



			


		
		print "Case #" + str(i) + ": " + str(max(ls,rs)) + " " + str(min(ls,rs))





