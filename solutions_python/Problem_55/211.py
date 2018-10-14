fin = open('C-small-attempt0.in', 'r')
fout = open('C-small.out', 'w')

for t in range(int(fin.readline())):
    runs, cpc, n = [int(a) for a in fin.readline().split(' ')]
    groups = [int(a) for a in fin.readline().split(' ')]

    moneymade = 0
    onride = []
    for i in range(runs):
        curcpc = cpc
        groups += onride
        onride = []
        while len(groups)>0 and groups[0] <= curcpc:
            moneymade += groups[0]
            curcpc -= groups[0]
            onride.append(groups[0])
            groups.remove(groups[0])
            
        
    print('Case #', t+1, ': ', moneymade, sep='', file=fout)

fin.close()
fout.close()
