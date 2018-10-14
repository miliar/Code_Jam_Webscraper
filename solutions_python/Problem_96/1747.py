import sys

def googlers(surprises, totalpoints, bestvalue):
	results = []
	for point in totalpoints:
		triplets = []
		first = point/3
		remainder = abs(point - first)
		second = remainder/2
		third = abs(remainder - second)
		triplets = [first, second, third]
		triplets.sort()
		results.append(triplets)

	for x in results:
		if abs(x[0]-x[1]) >= 3 | abs(x[0]-x[2]) >= 3 | abs(x[2]-x[1]) >= 3:
			summation = (x[2] + x[0])
			x[0] = summation/2
			x[2] = abs(summation - x[0])
			x.sort()
			continue
		else:
			continue

        print results
	count = 0
	i = len(results) - 1

	while i >= 0:
            if count != surprises:
                if abs(results[i][0] - results[i][1]) == 2 | abs(results[i][0] - results[i][2]) == 2 | abs(results[i][2] - results[i][1]) == 2:
                        count += 1
                else:
                        sideA = abs(results[i][2] - results[i][0])
                        sideB = abs(results[i][2] - results[i][1])
                        if  sideA > sideB | sideB < sideA:
                                if (results[i][2] + 1) <= 10 | (results[i][1] - 1) >= 0:
                                        if abs((results[i][2] + 1) - (results[i][1]-1) < 3) & abs((results[i][2] + 1) - results[i][0]) < 3:
                                                maxi = max([results[i][2] + 1, results[i][1] - 1, results[i][0]])
#                                                mini = mini([results[i][2] + 1, results[i][1] - 1, results[i][0]])
                                                if maxi >= bestvalue:
                                                        results[i][2] += 1
                                                        results[i][1] -= 1
                                                        count += 1
                                        else:
                                                if abs((results[i][1] + 1) - results[i][2]) < 3 & abs((results[i][1] + 1) - (results[i][0] - 1)) < 3:
                                                        if bestvalue <= max([results[i][2], results[i][1] + 1, results[i][0] - 1]):
                                                                result[i][1] += 1
                                                                result[i][0] -= 1
                                                                count += 1

                                elif (results[i][1] + 1) <= 10 | (results[i][0] - 1) >= 0:
                                        if abs((results[i][1] + 1) - results[i][2]) < 3 | abs((results[i][1] + 1) - (results[i][0] - 1)) < 3:
                                                if bestvalue <= max([results[i][2], results[i][1] + 1, results[i][0] - 1]):
                                                        results[i][1] += 1
                                                        results[i][0] -= 1
                                                        count += 1
                                else: pass

                        if sideA == sideB :
                                if (results[i][1] + 1) <= 10 | (results[i][0] - 1) >= 0:
                                        if bestvalue <= max([results[i][1] + 1, results[i][2], results[i][0]-1]):
                                                results[i][1] += 1
                                                results[i][0] -= 1
                                                count += 1
            i -= 1
        print results
	maxcount = 0
	for x in results:
		if max(x) >= bestvalue:
			maxcount += 1

	return maxcount

if __name__ == "__main__":
    f = sys.stdin
    output = open('B-small.txt', 'w')
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)
   
    test = int(f.readline())
    for t in xrange(test):
        n = f.readline().split()
        points = [int(n[3+i]) for i in xrange(0, int(n[0]))]
#        print points
        output.write("Case #%d: %d \n" % (t+1, googlers(int(n[1]), points, int(n[2]))))

    output.close()
#    print bestresult(0, [0], 0)