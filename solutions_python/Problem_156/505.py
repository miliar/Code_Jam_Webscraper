# ___ ______________________________________________ ___ #
#|_/*|                                              |*\_|#
#|_/*|    Google Code Jam - "Hello World"           |*\_|#
#|_/*|    10.04.2015 - the end                      |*\_|#
#|_/*|    Qualification                             |*\_|#
#|_/*|______________________________________________|*\_|#
#|                                                      |#
#|        Denis Werner - denis@nobbd.de                 |#
#|______________________________________________________|#
#                                                        #
import math

filename = "B-large.in"
filename = "B-small.in"
filename = "B-small-attempt6.in"

lines = ()
with open(filename) as file:
	lines = file.read().splitlines()

number_of_sets = int(lines[0])

with open(filename+".solved","w") as outputfile:
	for i in range(0,number_of_sets):


		eaters = int(lines[i*2+1])
		plates = map(int,lines[i*2+2].split(" "))
		solved = False
		rounds = 0
		max_init = max(plates)
		print " "
		print "###### ROUND "+str(i+1)+" ########"
		while not solved:

			print plates

			#get max pancakes
			c = max(plates)
			# create log-list for current plates list
			log_list = [0]*(c+1)
			for li in range(0,c+1):
				log_list[li] = li

			for base in range(2,c):
				#print "base:"+str(base)
				for pi in range(0,len(plates)):
					current_p = plates[pi]
					#print "pi: "+str(current_p)
					if current_p > base:
						#cur_log = int(math.log(current_p,base))
						cur_log = float(current_p)/base
						#print "log: "+str(cur_log)
						log_list[base] += max(1,cur_log-1)
			print "log list: " + str(log_list)

			log_list = log_list[2:]
			if log_list:
				new_best = len(log_list) - log_list[::-1].index(min(log_list)) + 1
				#best_split = log_list.index(min(log_list)) + 2
				best_split = new_best
				print "Best split till: " + str(best_split)
				#print "new: " + str(new_best)
				print "max: "+str(c)
				print c==best_split
				if c == best_split:
					solved = True
					rounds += best_split
				else:
					for pi in range(0,len(plates)):
						p = plates[pi]
						if p > best_split:
							print str(p)+" splitted."
							rounds += 1
							plates.append(best_split)
							plates[pi] -= best_split
			else:
				rounds += c
				solved = True
				print "Solved no log list"


		if rounds > max_init:
			print "rounds bigger then max"
			rounds = max_init

			
		
		# number of plates with > p/2 pancakes < p/2 then split

		line = "Case #"+str(i+1)+": "+str(int(rounds))
		print line
		outputfile.write(line+"\n")				
					