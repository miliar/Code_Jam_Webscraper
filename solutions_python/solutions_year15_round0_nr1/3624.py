DEBUG = False

def debug(string):
	if DEBUG:
		print(string)

T = int(input())



for i in range(0,T):
	line = input().split(" ")
	#debug(line)
	smax = line[0]
	audience = line[1].strip()
	added = 0
	active = 0
	if i == 2:
		DEBUG = False
	#debug("Audience: "+audience)
	for (level,n) in enumerate(audience):
		level = int(level)
		n = int(n)
		debug("Active: "+str(active))
		debug("N: "+str(n))
		debug("level: "+str(level))
		debug("Added: "+str(added))

		if level == 0:
			active += n
		else:
			if active < level:
				missing = level-active
				active += missing+n
				added +=missing
			else:
				active += n
		debug("postActive: "+str(active))
		debug("postN: "+str(n))
		debug("postlevel: "+str(level))
		debug("postAdded: "+str(added))

		debug("###########")
	print("Case #%d: %d"%(i+1,added))
