import os

ON = True
OFF = not ON

MAX_K = 100
MAX_N = 10

def print_table(n):

    for i,v  in enumerate(n) :
        print 'N = %d: ' % (i + 1),
        for e in v:
            if e[0] == ON:
                s = 'ON'
            else:
                s = 'OFF'

            print '(%s,' % s,

            if e[1] == ON:
                s = 'YES'
            else:
                s = 'NO'
            print '%s),' %s,
        print
                


def build_table(n, N, K):

    tablelen = len(n)
    while N > tablelen:
        n.append([[False, False]])
        tablelen += 1
    
    for i in xrange(N):
        k = len(n[i])
        if K > k - 1:
            for j in xrange(k, K + 1):
                if i == 0:
                    n[i].append([not n[i][j-1][0], not n[i][j-1][1]])
                else:
                    entry = [n[i][j-1][0], n[i][j-1][1]]
                    if n[i - 1][j - 1][0] and n[i - 1][j - 1][1]:
                        entry[0] = not entry[0]

                    if n[i - 1][j][1] and entry[0]:
                        entry[1] = True
                    else:
                        entry[1] = False

                    n[i].append(entry)        
        
    

def main(f):
    fo = open(f, 'r')
    output = open(f + '.out', 'w')
    numtests = int(fo.readline())
    for i in xrange(numtests):
        
        N, K = tuple([int(x) for x in fo.readline().split()])
        #print 'N', N, 'K', K
        # simple dynamic programming solution
        table = []
        light_state = 'OFF'
        if len(table) == 0 or (len(table) > 0 and K >= len(table[0])):
            build_table(table, N, K)

        #print_table(table)
        if table[N -1][K][0] and table[N-1][K][1]:
            light_state = 'ON'

        #print table
        output.write( 'Case #%d: %s' % (i + 1, light_state))
        output.write('\n')

    fo.close()
    output.close()
  

if __name__ == '__main__':
    main('qn.in')
