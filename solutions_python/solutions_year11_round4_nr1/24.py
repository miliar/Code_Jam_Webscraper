import copy

infile = open('A-large.in').readlines()
infile = [line.strip() for line in infile]
wfile = open('result', 'w')
T = int(infile[0])
infile = infile[1:]

for case_no in range(1, T+1):
    line = infile[0]
    infile = infile[1:]
    X, S, R, t, N = [int(x) for x in line.split()]
    S = S * 1.0
    R = R * 1.0
    t = t * 1.0
    lines = infile[:N]
    infile = infile[N:]
    wk = []
    for line in lines:
        tmp = [int(x) for x in line.split()]
        wk.append(tmp)
        
    wk.sort(key = lambda x: x[0])
    zero = 0
    start = 0
    for a, b, c in wk:
        if a != start:
            zero += (a - start)
            
        start = b
        
    if start < X:
        zero += (X- start)
        
    time = 0
    if t <= zero / R:
        time += t
        zero -= (R * t)
        time += (zero / S)
        for a, b, c in wk:
            time += ((b-a) / (c+S))
            
        wfile.write('Case #%s: %s\n' % (case_no, time))
        continue
    
    time += (zero / R)
    t -= (zero/R)
    wk.sort(key = lambda x: x[2])
    for a, b, c in wk:
        if t == 0:
            time += ((b-a) / (c+S))
        else:
            if (b-a) / (c+R) < t:
                t -= (b-a) / (c+R)
                time += (b-a) / (c+R)
                
            else:
                time = time + t + (b-a-t*(c+R)) / (c+S)
                t = 0
                
    wfile.write('Case #%s: %s\n' % (case_no, time))
    
    
    
    
    
        
    