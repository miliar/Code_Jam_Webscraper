import math
#yoloswag
def solve(smax, kList):
    f = 0
    total = int(kList[0])
    for i in range(1, len(kList)):
        p = int(kList[i])
        
        if(total < i):
            diff = i - total
            f += diff
            total += diff
        total += p
    return f

inputs = open("input.txt").readlines()
output = open('out.txt', 'w')
t = int(inputs[0])
r = 0
for i in range(1, t + 1):
	r += 1
	line = inputs[r].rstrip().split(" ")
	smax = line[0]
	kList = line[1]
	ans = solve(smax, kList)
	
	answer = "Case #%d: %d\n"%(i, ans)
	print(answer)
	output.write(answer)
output.close()
