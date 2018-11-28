'''
Theme Park Program
'''

r = open('C:/users/hasmeet/desktop/C-small-attempt0.in', 'r')

w = open('output.txt', 'w')

answer = ''

numCases = int(r.readline())

for i in range(numCases):
    first = r.readline().split(' ')
    groups = r.readline().split(' ')
    for k in range(len(groups)): groups[k] = int(groups[k])
    numRides = int(first[0])
    numpplPerRide = int(first[1])
    numGrps = int(first[2])
    answer += 'Case #' + str(i+1) + ': '
    totalNumppl = 0
    for g in groups: totalNumppl += g
    if totalNumppl <= numpplPerRide:
        answer += str(totalNumppl * numRides) + '\n'
        continue
    sums = {}
    profit = 0
    for p in range(numGrps):
        tot = 0
        futTot = 0
        ind = p
        while futTot <= numpplPerRide:
            tot = futTot
            futTot += groups[ind]
            ind = (ind + 1) % numGrps
        sums.update({p:(tot, (ind-1)%numGrps)})
    pos = 0
    for h in xrange(numRides):
        temp = sums[pos]
        pos = temp[1]
        profit += temp[0]
    answer += str(profit) + '\n'
    
w.write(answer)
r.close()
w.close()
print 'done'