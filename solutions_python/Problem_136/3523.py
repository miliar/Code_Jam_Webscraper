__author__ = 'tivvit'

file = open('B-small-attempt0.in')
outf = open('output.out', 'w')

cases = int(file.readline())
runnedCases = 1
while runnedCases <= cases:
    array = file.readline().split()
    c, f, x = [float(str(i)) for i in array]
    '''
    c = float(array[0])
    f = float(array[1])
    x = float(array[2])
    '''
    #print c, f, x

    min = float("inf")
    n = 0.
    g = 2.

    while True:
        t = x/((n*f)+g)
        #print t, n
        nc = n
        #print nc
        while nc > 0:
            nc -= 1
            t += c/(g+(nc*f))
            #print "-"*int(nc), t


        if t < min:
            min = t
        else:
            break


        n += 1



    out = "Case #" + str(runnedCases) + ": "
    out += '{0:.7f}'.format(min)

    print out
    outf.write(out + '\n')

    runnedCases += 1

file.close()
outf.close()