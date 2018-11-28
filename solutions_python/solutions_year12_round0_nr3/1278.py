import sys

i = open("C-small-attempt0.in", "r")
T = int(i.readline())
for X in range(T):
    L = []
    line = i.readline().strip().split()
    A = int(line[0])
    B = int(line[1])
    numbers = []
    for number in range(A, B+1):
        numbers.append(str(number))
    Y = 0
    i1 = 0
    prev = {}
    while i1 < len(numbers):
        i2 = 1
        while i2 < len(numbers[i1]):
            if ((numbers[i1][i2:] + numbers[i1][:i2]) in numbers) and not ((numbers[i1][i2:] + numbers[i1][:i2]) == numbers[i1]) and not ((numbers[i1], numbers[i1][i2:] + numbers[i1][:i2]) in prev):
                Y += 1
                prev[(numbers[i1], numbers[i1][i2:] + numbers[i1][:i2])] = ''
            i2 += 1
        numbers.pop(i1)
    print "Case #%d: %d" % (X+1, Y)
    
                
    
    
        