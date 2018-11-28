import math

def main(f):
    inFile = open(f)
    
    c = int(inFile.readline())

    r = []
    for i in range(0, c):
        line = inFile.readline()
        v = map(lambda x: int(x), line.split(' '))

        [N, S, P, t] = [v[0], v[1], v[2], v[3:]]

        res = 0
        
        for j in t:
            if j > 0:
                m = int(j/3)
                k = j - m*3

                if k>0:
                    m += 1
                
                if m >= P:
                    res += 1
                elif m+1 >= P and S>0 and (k==2 or k==0):
                    S -= 1
                    res += 1
            elif P==0:
                res += 1
                
        r.append(res)

    outFile = open(f.replace('.in', '.out'), 'w')
    for i in range(0, c):
        outFile.write('Case #%d: %d\n' % ((i+1), r[i]))
    outFile.close

if __name__ == '__main__':
    main('c:/jam/2012/B-large.in')

