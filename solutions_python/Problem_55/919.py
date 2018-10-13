'''
Created on 09-May-2010

@author: ashwin.saraf
'''

f = open('C://C-small.in')
output = open('C://output.txt', 'w')
cases = int(f.readline())
for case in range(cases):
    RkN = f.readline().split(' ')    
    R = int(RkN[0])
    k = int(RkN[1])
    N = int(RkN[2])
    queue = (f.readline().split(' '))
    cash = 0
    for run in range(R):
        numberToBeSeated = 0
        groupCount = 0
        while numberToBeSeated < k and groupCount < N:
            groupCount = groupCount + 1
            if numberToBeSeated + int(queue[0]) > k:
                break
            goingIn = int(queue.pop(0))
            queue.append(goingIn)
            numberToBeSeated = numberToBeSeated + goingIn
        cash = cash + numberToBeSeated
    output.write('Case #'+ str(case+1) +": " + str(cash) +"\n")