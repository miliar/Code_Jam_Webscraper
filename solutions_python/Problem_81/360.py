fname = 'A-large'
fin = open(fname + '.in', 'r')
fout = open(fname + '.out', 'w')

def calc_wp(record, team=-1):
    wins = 0.0
    total = 0.0
    for i in range(len(record)):
        if i <> team:
            if record[i] == '.':
                continue
            else:
                total += 1
            if record[i] == '1':
                wins += 1

    return wins/total
    

T = int(fin.readline())
for i in range(T):
    
    N = int(fin.readline())
    schedule = [['']*N for x in range(N)]
    wp = [0]*N
    owp = [0]*N
    num_opp = [0]*N
    oowp = [0]*N
    
    for j in range(N):
        schedule[j] = fin.readline()[:N]

        wp[j] = calc_wp(schedule[j])

    for j in range(N):
        for k in range(N):           
            if schedule[j][k] != '.':
                owp[k] += calc_wp(schedule[j], k)
                num_opp[k] += 1

    for j in range(N):
        owp[j] /= num_opp[j]
        
    for j in range(N):
        for k in range(N):
            if schedule[j][k] != '.':
                oowp[j] += owp[k]

        oowp[j] /= num_opp[j]
    
    fout.write('Case #{0}:\n'.format(i+1))
    for j in range(N):
        fout.write(str( (0.25*wp[j]) + (0.5 * owp[j]) + (0.25 * oowp[j])) + '\n')
        
fin.close()
fout.close()
    
