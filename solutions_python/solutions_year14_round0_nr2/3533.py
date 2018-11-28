f = open('B-small-attempt0.in', 'ro')
g = open('B-small-attempt0.out', 'w')

input = f.readlines()
casecnt = input[0]

for i in xrange(int(casecnt)):
    base_time = float("inf")
    cur_time = 0.0
    farm = 0
    C = float(input[i+1].split()[0])
    F = float(input[i+1].split()[1])
    X = float(input[i+1].split()[2])
    while (True):
        farm_time = 0
        if farm == 0:
            cur_time = X/(2+(farm * F))
        else:
            for j in xrange(farm):
                farm_time += C/(2+(j*F)) 
                cur_time = farm_time+X/(2+(farm * F))
        if cur_time < base_time:
            base_time = cur_time
            farm += 1
        else:
            result = "%.7f" % base_time
            break
    g.write('Case #' + str(i+1) + ': '+ result +'\n')
