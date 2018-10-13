fi = open('/tmp/B-large.in', 'r')
n = int(fi.readline())
answer = []
ctr = n
while ctr > 0:
    noD = int(fi.readline())
    noP = fi.readline().split()
    noP = [int(x) for x in noP]
    ans = max(noP)
    q = 2
    while q <ans:
        ans = min (ans, sum([(x - 1 ) // q for x in noP]) + q)
        q += 1
    answer.append(ans)
    ctr -= 1 
fo = open('/home/akshay/Desktop/codejam2.txt', 'w')
for i in range(n):
    fo.write('Case #' + str(i + 1) + ': ' + str(answer[i]) + '\n')
fo.close()
