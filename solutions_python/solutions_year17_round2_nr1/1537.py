# filenames
filein = "A-large.in"
fileout = "A-test-large.answers"

answers = open(fileout, 'w')
with open(filein) as file:
    T = int(file.readline())
    t = 0
    while t < T:
        D,N = file.readline().split()
        maxTime = 0
        D = int(D)
        N = int(N)
        n = 0
        while n < N:
            start, speed = file.readline().split()
            newTime = (D - int(start)) / int(speed)
            if newTime > maxTime:
                maxTime = newTime
            n += 1
        answers.write("case #" + str(t+1) + ": " + str(D / maxTime) + '\n')
        t += 1
