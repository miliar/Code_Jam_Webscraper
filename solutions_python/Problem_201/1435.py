with open('C-large.in') as f:
	t = int(f.readline())  # read a line with a single integer
	i = 0
	for line in f:
		i += 1
  		N, K = [int(s) for s in line.split(' ')]  # read a list of integers, 2 in this case
  		if N==K:
  			print "Case #{}: 0 0".format(i)
  			continue
  		maxmax = 0
  		minmax = 0
  		n = N
  		k = K
  		while True:
  			n -= 1
  			k -= 1
  			lStalls = n // 2
  			rStalls = n - lStalls

  			lPeople = k // 2
  			rPeople = k - lPeople
  			if k == 0:
  				maxmax = rStalls
  				minmax = lStalls
  				break
  			if k == 1:
  				n = rStalls
  				k = 1
  				continue
  			if n%2==0:
  				n = rStalls
  				k = rPeople
  				continue
  			else:
  				if k%2==0:
  					n = lStalls
  					k = lPeople
  					continue
  				else:
  					n = rStalls
  					k = rPeople
  					continue

  		print "Case #{}: {} {}".format(i, maxmax , minmax)

