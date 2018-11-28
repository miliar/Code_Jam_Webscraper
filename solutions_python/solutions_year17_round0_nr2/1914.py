t = int(input())
outputlist = [0]*t
for i in range(t):
    n = int(input())
    nlength = len(str(n))
    loopidx = 1

    if nlength == 1:
        outputlist[i] = 'Case #' + str(i+1) + ': ' + str(n)
    else:
        while loopidx < nlength:
            smallerbase = (n%(10**loopidx))//10**(loopidx-1)
            largerbase = (n%(10**(loopidx+1)))//10**(loopidx)
            if smallerbase < largerbase:
                n = (n//(10**loopidx) - 1)*(10**loopidx) + (10**loopidx - 1)
            loopidx += 1

        outputlist[i] = 'Case #' + str(i+1) + ': ' + str(n)

for i in range(t):
    print(outputlist[i])
