import sys


def guestsNeeded(S, data):
	#print (S, data)
	if S == 0:
		return (int(data[0]), 0); # all rise, none stay seated.
	else:
		#return (int(data[S]), int(data[S])+guestsNeeded(S-1, data)[1], 0) if guestsNeeded(S-1, data)[0] >= S else  (int(data[S]), int(data[S])+guestsNeeded(S-1, data)[1], int(data[S])+guestsNeeded(S-1, data) )
		people_at_this_level = int(data[S])
		people_risen, guest_needed_so_far = guestsNeeded(S - 1, data)
		if people_risen >= S:
			# everyone at this level rises too!
			return (people_risen + people_at_this_level, guest_needed_so_far)
		else:
			#print ("S", S, "people_risen: ", people_risen, "people_at_this_level: ", people_at_this_level, "guest_needed_so_far: ", guest_needed_so_far)
			if (people_at_this_level == 0):
				return (people_risen, guest_needed_so_far)
			return (people_risen + people_at_this_level +((S - people_risen) + guest_needed_so_far), (S - people_risen) + guest_needed_so_far)


#print guestsNeeded(6, "0200012")
idx = 1
line = sys.stdin.readline()
cases = int(line )
while idx <= cases:
    line = sys.stdin.readline()
    Smax, data = line.split()
    print "Case #" + str(idx)+":", guestsNeeded(int(Smax), data)[1]
    idx+=1
