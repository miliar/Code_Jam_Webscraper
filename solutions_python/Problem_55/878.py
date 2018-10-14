def roller(filename):
	f = open(filename, 'r')
	num_test = int(f.readline())
	
	for i in range(num_test):
		line = f.readline()
		if not line: break
		R, k, N = map(int, line.split())
		line = f.readline()
		groups = map(int, line.split())
		result = money(R, k, groups)
		print "Case #" + str(i+1) + ": " + str(result)

def money(R, k, groups):
	totalriders = 0
	for r in range(R):
		#print "ride number", r, "!", k, "people are allowed"
		# How many people fit on the roller coaster?
		riders = 0
		for g in range(len(groups)):	# a group can't go on more than once in a ride!
			nextgroup = groups[0]
			if nextgroup < k - riders + 1:
				riders = riders + nextgroup
				#print "group size", nextgroup, "is going. Total size is now", riders
				groups.pop(0)
				groups.append(nextgroup)
				#print groups
			else:
				break	# Run the roller coaster!
		totalriders = totalriders + riders
		#print "Total riders:", totalriders
	return totalriders
		

if __name__ == "__main__":
	roller("C-small-attempt0.in")
