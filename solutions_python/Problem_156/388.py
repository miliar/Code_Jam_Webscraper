import csv
from collections import Counter
from math import ceil

fin = open('../Downloads/B-large.in','r');
#fin = open('input.in','r');
fout = open('output.out','w');

data = csv.reader(fin, delimiter=' ')
T = int(next(data)[0]);

for k in range(T):
    print('{} of {}'.format(k, T));
    D = int(next(data)[0]);
    P = next(data);
    P = [int(p) for p in P];
    N = Counter(P)
    #Create structure with all (P_j, N_j);
    Pmax = max(N.keys());
    tmin = Pmax;
    n = Pmax;
    #print('tmin = {}'.format(tmin));
    for n in range(Pmax-1,0,-1):
        t = sum([Nj*(ceil(Pj/n)-1) for Pj, Nj in zip(N.keys(), N.values())])+n;
        #print('sum + n = {}+{} = {}'.format(sum([Nj*(ceil(Pj/n)-1) for Pj, Nj in zip(N.keys(), N.values())]), n, t));
        if t<tmin:
            tmin = t;
            #print('tmin = {}'.format(tmin));
    fout.write('Case #{}: {}'.format(k+1, tmin));
    if k+1<T:
        fout.write('\n');

fout.close();
del data;
fin.close();
