datain = open('A-small-attempt0.in', 'r')
dataout = open('dataout.txt', 'w')

for length in range(1, int(datain.readline()) + 1):

    rVal, eVal = map(int, datain.readline().split())
    
    count = 0
    
    while eVal > 0:
        eVal -= ((rVal+1)**2 - rVal**2)
        if eVal >= 0:
            count += 1
        rVal += 2
    print 'Case', length, 'count', count
    
    dataout.write('Case #' + str(length) + ': ' + str(count) + '\r')

datain.close()
dataout.close()