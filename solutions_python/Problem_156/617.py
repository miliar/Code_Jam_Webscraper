fi = open('/home/pi/Downloads/B-large.in', 'r')
n = int(fi.readline())
answer = []
ctr = n
while ctr > 0:
	noD = int(fi.readline())
	noP = fi.readline().split()
	noP = [int(x) for x in noP]
	ans = max(noP)
	Z = 2
	while Z <ans:
		ans = min (ans, sum([(x - 1 ) // Z for x in noP]) + Z)
		Z += 1
	answer.append(ans)
	ctr -= 1 
fo = open('/home/pi/Downloads/OUTPUTYEAHLARGE.txt', 'w')
for i in range(n):
	fo.write('Case #' + str(i + 1) + ': ' + str(answer[i]) + '\n')
fo.close()
