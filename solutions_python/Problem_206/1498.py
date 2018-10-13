	

if __name__ == "__main__":

	t = int(raw_input())
	for i in range(1,t+1):
		line_item = raw_input().split(" ")
		d = int(line_item[0])
		n = int(line_item[1])
		
		k = []
		s = []
		for j in range(0,n):
			#read in n horse details
			horse_det = raw_input().split(" ")
			k.append(int(horse_det[0]))
			s.append(int(horse_det[1]))
			
#		print k,s

		#small dataset
#		if n == 1:
#			t = (d-k[0])/(s[0]*1.0)
#			print t
#			a = d/t
			
			
#		if n == 2:
#			t1 = (d-k[0])/(s[0]*1.0)
#			print t1
#			t2 = (d-k[1])/(s[1]*1.0)
#			print t2
			
#			if t1 > t2:
				#ie first horse (closer to start) does not cross second 
				#we should consider time of first horse
#				a = d/(t1*1.0)
#			else:#consider slower horse time
#				a = (d*1.0)/(max(t1,t2))

#		if n > 2:
		if 1:
			#create tuple for each horse
			hl = zip(k,s)
			#first find slowest horse (first instance)
			#sort list to have horses in irder of pos from start
#			print hl, len(hl)
			itr = 0
			while (len(hl)!=0):
				itr = itr+1
#				print itr
				hl.sort(key=lambda x:x[0])
				hl_sorted = [list(x) for x in zip(*hl)]
				k_sorted = hl_sorted[0]
				s_sorted = hl_sorted[1]

				slowindex = s_sorted.index(min(s_sorted))
				timeslow = (d-k_sorted[slowindex])/(s_sorted[slowindex]*1.0)

				#find if crossover for all horses before slowest 
				#1 => no cross
				t_sorted_index = [1 if ((d-k_sorted[x])/(s_sorted[x]*1.0)>=timeslow) else 0 for x in range(0,slowindex)]
				
				#no cross horses are the new sublist to consider
				newhl = [hl[x] for x in range(0,len(t_sorted_index)) if t_sorted_index[x] == 1]
				hl = newhl

#			if itr == 0:
#				print "no loop"
			#when out last timeslow should be the concerned time
			a = (d*1.0)/(timeslow)



		print "Case #" + str(i) + ": " + str(a)

