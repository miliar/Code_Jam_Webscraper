import copy

infile = open('A-large.in').readlines()
infile = [line.strip() for line in infile]
wfile = open('result', 'w')
T = int(infile[0])
infile = infile[1:]

def calwp(games):
    wp = []
    # wp
    for line in games:
        tmp = line.replace('.', '')
        g = len(tmp) * 1.0
        w = sum([int(x) for x in list(tmp)])
        wp.append(w/g)
        
    return wp


for case_no in range(1, T+1):
    N = int(infile[0])
    infile = infile[1:]
    games = infile[:N]
    infile = infile[N:]
    #wp
    wp = calwp(games)
    
    #owp
    tmpwp = []
    for i in range(N):
        #throw out ith team
        tmp = copy.copy(games)
        for j in range(N):
            tmpj = list(tmp[j])
            tmpj[i] = '.'
            tmp[j] = ''.join(tmpj)
        tmpwp.append(calwp(tmp))
    owp = []
    for i in range(N):
        line = games[i]
        count = 0
        s = 0
        for j in range(N):
            if line[j] == '.':
                continue
            count += 1
            s += tmpwp[i][j]
        if count == 0:
            owp.append(0.0)
        else:
            owp.append(s/count)
            
    #oowp
    oowp = []
    for i in range(N):
        line = games[i]
        count = 0
        s = 0
        for j in range(N):
            if line[j] == '.':
                continue
            count += 1
            s += owp[j]
            
        if count==0:
            oowp.append(0.0)
        else:
            oowp.append(s/count)
            
    RPI = []
    for i in range(N):
        RPI.append(0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i])
        
    wfile.write('Case #%s:\n' % case_no)
    for i in range(N):
        wfile.write(str(RPI[i]) + '\n')
wfile.close()
        
        
        
        
        
        
        
        
        
        
        
        
            
        