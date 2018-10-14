fin = open('in', 'r')
fout = open('out', 'w')

numberOfCases = int(fin.readline())



for case in range(1,numberOfCases + 1):
    line = fin.readline()
    arr = line.split()
    arr = [float(string) for string in arr]
    currSpeed = 2
    timeWithoutFactory = arr[2]/2
    timeForFactories = arr[0]/currSpeed
    timeWithFactory = timeForFactories + arr[2]/(currSpeed+arr[1])
    while timeWithoutFactory > timeWithFactory:
        timeWithoutFactory = timeWithFactory
        currSpeed += arr[1]
        timeForFactories += arr[0]/currSpeed
        timeWithFactory = timeForFactories + arr[2]/(currSpeed+arr[1])
    fout.write('case #' + str(case) + ': ' + str(timeWithoutFactory) + '\n')




fin.close()
fout.close()


