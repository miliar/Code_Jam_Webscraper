inputfile = open('A-small-attempt0.in', 'r')
outputfile = open('A-small-attempt0.out', 'w')
n = int(inputfile.readline())

for i in range(n):
    [r, t] = inputfile.readline().split(' ')
    [r,t] = [int(r),int(t)]
    
    j = 1
    count = 0
    
    while t > 0:
        if t >= (r + j)**2 - (r + j - 1)**2:
            t -= (r + j)**2 - (r + j - 1)**2
            j += 2
            count += 1
        else:
            break
    outputfile.write("Case #" + str(i + 1) + ": " + str(count) + "\n")
