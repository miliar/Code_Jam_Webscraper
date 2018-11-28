import itertools

o = open('B-small-attempt1.out', 'w')

with open('B-small-attempt1.in') as f:
    n = [int(x) for x in f.readline().split()] # read first line
    array = []
    i = 1
    for line in f: # read rest of lines
        a, b, k = ([int(x) for x in line.split()])
        al = list(range(0,a))
        bl = list(range(0,b))
        abl = itertools.product(al,bl)
        l = 0
        for el in abl:
            if el[0] & el[1] < k:
                l += 1
        o.write('Case #' + str(i) + ': '+ str(l) + '\n')
        i += 1
        

o.close()
