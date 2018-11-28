#!/usr/bin/python
import sys

if __name__ == '__main__':
		N = int(sys.stdin.readline().strip())
		
		for i in range (1,N+1):
			S = int(sys.stdin.readline().strip())
			engines = []
			phrases = []
			for j in range(1,S+1):
				engines.append(sys.stdin.readline().strip())
			
			Q = int(sys.stdin.readline().strip())
			for j in range(1,Q+1):
					phrases.append(sys.stdin.readline().strip())
			
			if len(phrases) == 0:
				print "Case #%s: %s"%(str(i),str(0))
				continue

			start 		   = 0
			switches     = 0
			
			phrase_in = phrases[0]
			is_end      = False
			
			while start < len(phrases):
			
				for engine in engines:
					if engine != phrase_in:
						was_found = False
						for phrase in phrases[start+1:len(phrases)]:
							if engine == phrase:
								was_found = True
								break
						
						if was_found is False:
							is_end = True
							break
							
				if is_end 	is True:
					break
					
				maximum = 0
				for engine in engines:
						if engine != phrase_in:
							counter = start+1
							for phrase in phrases[start+1:len(phrases)]:
								if engine == phrase:
									if (counter > maximum) :
										maximum = counter
									break							
								counter+=1
							
				if maximum < len(phrases):
					switches+=1				
					
				phrase_in = phrases[maximum]	
				start = maximum
			
			
			print "Case #%s: %s"%(str(i),str(switches))
