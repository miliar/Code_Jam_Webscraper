T = input()
n=1
import string
while n<=T:
	rec = 0
	d = {}
	Text = raw_input()
	nums = Text.split()
	length = len(nums[0])
	if length == 1:
		print "Case #%d:"%n + " %d" %rec
	else:
		lower = int(nums[0])
		upper = int(nums[1])
		diginter = 1
		rang = range(lower,upper+1)
		while diginter < length:
			for incre in rang:
				sincre = str(incre)
				nusplit = list(sincre)
				nufront = nusplit[0:length-diginter]
				nuback = nusplit[length-diginter:length]
				nuback.extend(nufront)
				internum = ''.join(nuback)
				recnum = int(internum)
				if diginter == 1:
					if recnum in rang and incre < recnum:
						d[incre]=recnum
						rec = rec + 1
				elif recnum in rang and incre < recnum:
					if d.has_key(incre):
						if d[incre] != recnum:
							d[incre] = recnum
							rec = rec + 1
					else:
						rec = rec + 1
			diginter = diginter + 1
		print "Case #%d:"%n + " %d" %rec 
	n = n + 1
