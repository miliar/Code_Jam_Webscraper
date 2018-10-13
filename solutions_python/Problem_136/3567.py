fi = open('file.in', 'r')
numCases = int(fi.readline())

out = ''
for i in range(1, numCases + 1):
    vals = fi.readline().split()
    c = float(vals[0])
    f = float(vals[1])
    x = float(vals[2])

    rate = 2
    nextRate = rate + f
    time = x/rate
    nextTime = c/rate + x/nextRate
    
    while time - nextTime > .0000001:
        time = nextTime
        newNextRate = nextRate + f
        nextTime = nextTime - x/nextRate + c/nextRate + x/newNextRate
        rate = nextRate
        nextRate = newNextRate

    out += 'Case #' + str(i) + ': ' + str(time) + '\n'
fi.close()

fi = open('file.out', 'w')
fi.write(out)
fi.close()
