from bisect import bisect_left

T = int(raw_input())
results = []

# Need to actually count them all I think; presort (nlogn), then match Ken's to Naomi's
# Find the max(number of Naomi's blocks that are lighter than all of Ken's,
	# number of Ken's blocks that are heavier than all of Naomi's)

f = open("DeceitfulWarOut.txt", 'w')
for k in xrange(T):
	truthful = 0
	deceitful = 0
	N = int(raw_input())
	Naomi = map(float, raw_input().split())
	Ken = map(float, raw_input().split())
	Naomi.sort()
	Ken.sort()

	#truthful
	i = j = 0
	while j < N:
		if Ken[j] > Naomi[i]:
			truthful += 1
			i += 1
		j += 1
	
	#deceitful
	i = j = 0
	while i < N:
		if Naomi[i] > Ken[j]:
			deceitful += 1
			j += 1
		i += 1
	print >> f, "Case #{}: {} {}".format(k+1,deceitful, N-truthful)

f.close()


"""
	Kmin = min(Ken)
	Nmax = max(Naomi)
	i = left = right = 0
	j = N - 1
	while i <= N - 1:
		if Naomi[i] < Kmin:
			left += 1
			i += 1
		else:
			break
	while j >= 0:
		if Ken[j] > Nmax:
			right += 1
			j -= 1
		else:
			break
	deceitful = max(left,right)
"""