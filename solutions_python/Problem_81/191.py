#!/usr/bin/env python

def main():
    cases = int(raw_input())
    for case in xrange(cases):
        n = int(raw_input())
        score = ['' for i in xrange(n)]
        rpi = [0 for i in xrange(n)]
        w = [0 for i in xrange(n)]
        ow = [0 for i in xrange(n)]
        for i in xrange(n):
            score[i] = raw_input()
            
        for i in xrange(n):
            wp = owp = oowp = 0
            count = 0
            for j in xrange(n):
                if score[i][j] == '.':
                    continue
                wp = wp + (1 if score[i][j] == '1' else 0)
                #owp = owp + (1 if score[i][j] == '0' else 0)
                count += 1
                
            w[i] = float(wp) / count
            #ow[i] = float(owp) / count
        
        for i in xrange(n):
            owp = c = 0
            for j in xrange(n):
                if i != j and score[i][j] != '.':
                    wp = count = 0
                    for k in xrange(n):
                        if k != i and k != j:
                            wp += 1 if score[j][k] == '1' else 0
                            count += 1 if score[j][k] != '.' else 0
                    owp += (float(wp) / count) if count > 0 else 0
                    c += 1
            ow[i] = (float(owp) / c) #if c > 0 else 0
        
        for i in xrange(n):
            oowp = count = 0
            for j in xrange(n):
                if i != j and score[i][j] != '.':
                    oowp += ow[j]
                    count = count + 1
            oowp = float(oowp) / count
            rpi[i] = 0.25 * w[i] + 0.50 * ow[i] + 0.25 * oowp
            rpi[i] = str(rpi[i])
        
        print 'Case #%d:' % (case + 1)
        print '\n'.join(rpi)
    
if __name__ == '__main__':
    main()