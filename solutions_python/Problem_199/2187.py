import sys
def toStr(n,base):
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]

def flip(input, X, flipper):
    for i in range(0, flipper):
        input[X + i] = '+' if input[X + i] == '-' else '-'
    return input

#	orgN = list(N)
#	if X == 1:
#		N[0] = '+' if N[0] == '-' else '-'
#	else:
#		for i in range(0, X/2):
#			if i == 0 and N[i] == ('+' if N[X-i - 1] == '-' else '-'):
#				return flip(N, X-1)
#
#			temp = N[i]
#			N[i] = '+' if N[X-i - 1] == '-' else '-'
#			N[X-i - 1] = '+' if temp == '-' else '-'
#	
#		if X % 2 == 1:
#			N[X/2] = '+' if N[X/2] == '-' else '-'
#	if orgN == N:
#		return flip(N, X-1)
#	return N

def findIt(N, flipper):
    flips = 0
    #flipper = int(N[-1])
    #del N[-2:]
    if N[0] == '+' and N[1:] == N[:-1]:
		return 0
    else:
        #while not (N[0] == '+' and N[1:] == N[:-1]):
        for i in range(0, len(N)):
            for x in range(len(N) - flipper + 1):
                if N[0] == '+' and N[1:] == N[:-1]:
                    return flips
                
                #print N
                subList = N[x : x + flipper]
                #print subList
                if subList[0] == '-':
                    flips = flips + 1
                    N = flip(N, x, flipper)
    return -1

#                if subList[0] == '-' and subList[1:] == subList[:-1]:
#                    N = flip(N, x, flipper)
#                else:
#                    print "not combo :("
        #		for x in range(len(N) - 1, -1, -1):
        #	if N[x] == '-':
        #		N = flip(N, x + 1)
        #			print "NEXT"
        #		print N
        #		print x + 1
#		return findIt(N) + 1

results = []
firstLine = True
with open("A-large.in") as f:
	contents = f.readlines()
	for content in contents:
		if not firstLine:
			content = (content.strip("\n")).split(' ')
            #print content
			results.append(findIt(list(content[0]), int(content[1])))
                #results.append(findIt(list(content.strip("\n"))))
		firstLine = False;
	f.close()

file = open("a.out", "w")
counter = 1
for item in results:
	item = "IMPOSSIBLE" if item == -1 else item
	file.write("Case #" + str(counter) + ": " + str(item) + "\n")
	counter += 1

file.close()
