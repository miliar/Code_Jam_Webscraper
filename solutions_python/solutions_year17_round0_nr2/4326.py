f = open('B-large.in', 'r')
w = open("B-large.out","w")

Num_Tests = int(f.readline())
tstnum = 0
#for k in range(1,Num_Tests+1):
for line in f.readlines():
	tstnum = tstnum+1
	count = 0
	lst = []
	for c in line:
		if c.isdigit():
			count=count+1
			lst.append(int(c))
	lnlist = len(lst)
	#w.write(str(lst)+"\n")
	if lnlist == 1:
		ans = lst[0]
	else:
		broken = 0
		strans = ''
		for k in range(0, lnlist-1):
			if lst[k] > lst[k+1]:
				broken = 1
				if lst[k] == 1:
					for lp in range(1,lnlist):
						strans = strans+'9'
					ans = strans
					break
				else:
					lst[k] = lst[k]-1
					pm = k
					while (pm-1)>=0 and lst[pm-1]>lst[pm]:
						lst[pm] = 9
						lst[pm-1] = lst[pm-1]-1
						pm = pm-1
					for lp in range(0,k+1):
						strans = strans+str(lst[lp])
					#strans = strans + str(newd)
					for lp in range(k+1,lnlist):
						strans = strans+'9'
					ans = strans
					break
		if broken == 0:
			for lp in range(0,lnlist):
				strans = strans+str(lst[lp])
				ans = strans
	w.write("Case #"+str(tstnum)+": "+str(ans)+"\n")

f.close()
w.close()
