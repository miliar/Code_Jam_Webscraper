if __name__ == '__main__':
    infile = open('B-large.in').readlines()
    T = int(infile[0].strip())
    case_no = 0
    wfile = open('result', 'w')
    for line in infile[1:]:
        case_no += 1
        tmp = line.strip().split()
        C = int(tmp[0])
        tmp = tmp[1:]
        combs = {}
        for comb in tmp[:C]:
            combs[comb[:2]] = comb[2]
            combs[comb[1]+comb[0]] = comb[2]
        tmp = tmp[C:]
        D = int(tmp[0])
        tmp = tmp[1:]
        opps = {}
        for opp in tmp[:D]:
            if opp[0] not in opps:
                opps[opp[0]] = set()
            opps[opp[0]].add(opp[1])
            if opp[1] not in opps:
                opps[opp[1]] = set()
            opps[opp[1]].add(opp[0])
            
        string = tmp[-1]
        out = ''
        candi = set()
        for s in string:
            out += s
            if s in opps:
                candi.update(opps[s])
                
            if len(out) == 1:
                continue
            
            if out[-2:] in combs:
                out = out[:-2] + combs[out[-2:]]
                candi = set()
                for t in out:
                    if t in opps:
                        candi.update(opps[t])
                continue
                
            if s in candi:
                out = ''
                candi = set()
                continue
                
            
                
        wfile.write('Case #' + str(case_no) + ': ' + '[')
        wfile.write(', '.join(out) + ']\n')
    wfile.close()
        
        
        
        
        
        
        
        
        
        
        
        
        