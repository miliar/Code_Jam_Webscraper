input = """10
20 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
20 120 266 858 1243 1657 1771 2328 2490 2665 2894 3117 4210 4454 4943 5690 6170 7048 7125 9512 9600
20 4664 3076 13437 3034 48328 4376 4808 2866 1386 3518 4746 990 1054 1012 2166 216 2862 3792 680 3082
20 84387 35006 96938 54505 30819 82409 39351 64091 75216 23781 42976 88302 67532 14781 92703 81743 76882 66792 57533 44496
20 27600 21191 24072 94400 57573 39050 37354 2883 87804 91353 69498 42509 32632 18913 75616 60495 9798 14097 34113 86291
20 905 2461 4314 26 29456 887 2736 527 2259 2241 4134 285 1597 268 42 3043 719 341 1127 1544
20 2236 3360 3492 2792 45936 2422 3434 3278 878 2862 1166 1282 534 94301 3264 2396 4586 4250 2384 1320
20 86075 98926 13660 33056 73776 13320 69640 75194 1696 59228 69778 35983 58860 90781 22500 33986 50557 50033 1011 20437
20 32482 21338 80740 21870 1322 45897 72891 78873 47282 84682 16378 5979 92452 44272 57325 8923 46881 74602 19247 36498
20 96529 68223 71373 41481 24440 86022 9064 29053 51698 53549 50840 49975 90988 39696 20091 56192 88246 30101 90314 57840"""

lines = input.split("\n")

i=0
for l in lines[1:]:
	
	# Input i
	line = l.split(" ")
	
	N = int(line[0])
	ens = [int(s) for s in line[1:]]
	
	bound = pow(10,5)
	# print N, ens
	# Coder ici
	
	# E[j][k] : un sous-ensemble de [ens[0]..ens[j]] de somme k modulo 10e6
	E = [[] for j in range(0,N)]
	
	E[0] = [[] for j in range(0,bound)]
	E[0][ens[0]%bound] = [[ens[0]]]
	
	found = False
	for j in range(1,N):
		E[j] = [[] for k in range(0,bound)]
		E[j][ens[j]%bound] = [[ens[j]]]
		for s in range(0,bound):
			E[j][s] = E[j-1][s]+E[j][s]
			if len(E[j-1][s]) != 0:
				# il y avait un subset vaalnt s
				E[j][(s+ens[j])%bound] += [E[j-1][s][0]+[ens[j]]]
		for s in range(0,bound):
			if len(E[j][s])>1:
				# check if its real sumset
				s1 = sum(E[j][s][0])
				for subset in E[j][s][1:]:
					if sum(subset) == s1:
						# print "Sumset :"+str(E[j][s])
						found = True
						sol = E[j][s]
						break
			if found:
				break	
		if found:
			break
		
	r = ""
	for s in sol[0]:
		r += str(s)+" "
	r = r[:-1]+"\n"
	for s in sol[1]:
		r += str(s)+" "
	r = r[:-1]
	
	print "Case #"+str(i+1)+": \n"+r
	i += 1


def stringArrayToVector(arr):
	res = []
	for s in arr:
		res += [int(s)]
	return res