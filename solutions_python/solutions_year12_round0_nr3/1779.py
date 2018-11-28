#!/usr/bin/python

cases = []
results = []

times = int(raw_input())
for time in range(times):
	cases.append(raw_input())
i = 1
for case in cases:
	nums = case.split(" ")
	if (len(nums) != 2):
		result = 0
		results.append(0)
		continue

	numA = nums[0]
	numB = nums[1]

	allpairs = []
	for n in range(int(numA), int(numB)+1,1):
		strn = str(n)
		setn = set(strn)
		lstrn = len(strn)
		maxsetn = max(setn)
		countarray = {}
		if (lstrn != len(setn)):
			for char in setn:
				temp = strn.count(char)
				if (temp > 1):
					countarray[char] = temp
			deep = True
		else:
			deep = False
		maxBrange = numB
		for ind in range(0, lstrn):
			if (numA[ind] == numB[ind]):
				continue
			else:
				if (int(maxBrange[ind]) > int(maxsetn)):
					maxBrange = maxBrange[:ind] + (lstrn - ind) * str(maxsetn)
				break
		for m in range(n+1, int(maxBrange)+1,1):
			strm = str(m)
			go = True
	
			if (setn == set(strm)):
				if (deep == True):
					for char in countarray.keys():
						if ( countarray[char] != strm.count(char)):
							go = False
							break
			else:
				go = False
			if (go == True):
				value = False
				for index in range(lstrn-1, 0, -1):
					first = index
					last = lstrn-index
					if ((strn[first:] + strn[:first]) == strm):
						allpairs.append((n,m))
						break
	print "Case #" + str(i) + ": " + str(len(allpairs))	
	i += 1
