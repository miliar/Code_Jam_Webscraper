import math

def main():
    inFile = open('c:\jam\B-small-attempt5.in')

    T = int(inFile.readline())

    r = []
    for i in range(0, T):
        line = inFile.readline()

        print line        

        m = line[:-1].split(' ')
        k = int(m[0])

        comb = {}
        for j in range(0, k):
            s = m[1+j]
            u = s[:2]
            comb[u] = s[-1]
            u = s[1] + s[0]
            comb[u] = s[-1]

        kk = int(m[k+1])

        opp  = {}
        for j in range(0, kk):
            s = m[k+2+j]
            opp[s[0]] = s[1]
            opp[s[1]] = s[0]

        msg = m[-1]
        res = ''

        #print comb
        #print opp

        m = list(msg)
        q = []
        s = ''
        for i in range(0, len(m)):
            if len(q) > 0:
                s = q[-1] + m[i]
                if comb.has_key(s) == True:
                    q = q[:-1]
                    q.append(comb[s])
                else:
                    if opp.has_key(m[i]) == True:
                        u = opp[m[i]]

                        j = len(q) - 1
                        while j >= 0:
                            if q[j] == u:
                                q = []
                                break
                            j -=1

                        if j < 0:
                            q.append(m[i])

                    else:
                        q.append(m[i])
            else:
                q.append(m[i])
        
        res = ', '.join(n for n in q)       
        r.append(res)
        print res

    outFile = open('c:\jam\B-small-attempt5.out', 'w')
    for i in range(0, T):
        outFile.write('Case #%d: [%s]\n' % ((i+1), r[i]))
    outFile.close


if __name__ == '__main__':
    main()

