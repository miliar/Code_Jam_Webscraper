#!/usr/bin/python
import sys


def formatHour(hour):
		part1 = int(hour[0:2])
		part2 = int(hour[3:5])
		#print hour
		#print part1*60 + part2
		return int(part1*60 + part2)

if __name__ == '__main__':
		N = int(sys.stdin.readline().strip())
		
		for i in range (1,N+1):
			T = int(sys.stdin.readline().strip())
			deps = sys.stdin.readline().strip().split(' ')
			NA = int(deps[0])
			NB = int(deps[1])
			
			NA_times = []
			NB_times = []
			
			NA_ready = []
			NB_ready = []
			
			NA_deps = []
			NB_deps = []
			
			NA_counter = 0
			NB_counter = 0
			
			for j in range (1,NA+1):
				hours = sys.stdin.readline().strip().split(' ')
				NA_times.append( {'d' : formatHour(hours[0]) , 'a' : formatHour(hours[1]) })
				NA_ready.append(formatHour(hours[1])+T)
				NA_deps.append(formatHour(hours[0]))
				
				
			for j in range (1,NB+1):
				hours = sys.stdin.readline().strip().split(' ')
				NB_times.append( {'d' : formatHour(hours[0]) , 'a' : formatHour(hours[1]) })
				NB_ready.append(formatHour(hours[1])+T)
				
				NB_deps.append(formatHour(hours[0]))
				
			NA_deps.sort()	
			NB_deps.sort()
			NA_ready.sort()	
			NB_ready.sort()
			
			for element in NA_deps:
				is_train_ready = False
				positionToRemove = -1
				for iterator in range(0,len(NB_ready)):
						if NB_ready[iterator] <= element:
							is_train_ready = True
							positionToRemove = iterator
							break	
				if is_train_ready is False:
					NA_counter +=1				
				else:
					del NB_ready[positionToRemove]				
					
					
			for element in NB_deps:
				is_train_ready = False
				positionToRemove = -1
				for iterator in range(0,len(NA_ready)):
						if NA_ready[iterator] <= element:
							is_train_ready = True
							positionToRemove = iterator
							break	
				if is_train_ready is False:
					NB_counter +=1				
				else:
					del NA_ready[positionToRemove]						
				
			print "Case #%s: %s %s"%(str(i),str(NA_counter),str(NB_counter))
