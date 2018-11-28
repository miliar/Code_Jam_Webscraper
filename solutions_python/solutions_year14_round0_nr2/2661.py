def determine(params):
    C = float(params[0])
    F = float(params[1])
    X = float(params[2])
    
    time = 0
    farms = 0
    cookies = 0
    
    gameend = False
    while not gameend:
        rate = 2 + farms * F
        timeleft = X / rate
        timeinc = C / rate
        if timeleft > timeinc + X / (rate + F):
            time += timeinc
            farms += 1
        else:
            time += timeleft
            gameend = True
    
    return time
        
def processinput(filename):
    f = open(filename, 'r')
    cases = int(f.readline())
    
    input = []
    for i in range(cases):
        row = f.readline().split()
        input.append([float(x) for x in row])
    
    f.close()
    
    return input
    
def output(infile, outfile):
    f = open(outfile, 'w')
    
    counter = 0
    input = processinput(infile)
    for case in input:
        counter += 1
        f.write('Case #' + str(counter) + ': ' + str(determine(case)) + '\n')
        
    f.close()
    
output('B-large.in', 'B-large.out')