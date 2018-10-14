#filename = 'A-small-attempt0'
filename = 'A-large'

fin = open(filename + '.in', 'rb')
fout = open(filename + '.out', 'wb')

def read_int():
    return int(fin.readline())

def read_int_array():
    return [int(i) for i in fin.readline().split()]

T = read_int()

S = []
for i in xrange(T):
    N, S = fin.readline().split()
    ovating = int(S[0])
    invited = 0
    for j in xrange(1, len(S)):
        if int(S[j]) == 0:
            continue
        missing = j - ovating
        if missing > 0:
            invited += missing
            ovating += missing
        ovating += int(S[j])

    case = 'Case #%d: %d' % (i+1, invited)
    #print case
    fout.write(case + '\r\n')


fin.close()
fout.close()