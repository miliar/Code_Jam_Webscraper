import csv
from collections import Counter
from math import ceil

fin = open('../Downloads/A-large.in','r');
#fin = open('input.in','r');
fout = open('output.out','w');

data = csv.reader(fin, delimiter=' ')
T = int(next(data)[0]);

for k in range(T):
    print('{} of {}'.format(k, T));
    (Smax, S) = next(data);
    Smax = int(Smax);
    S = [int(s) for s in S];

    fmax = 0;
    ssum = 0;
    #print('tmin = {}'.format(tmin));
    for i in range(Smax+1):
        ssum += S[i];
        f = i - ssum + 1;
        #print('(i, ssum, f) = ({}, {}, {})'.format(i, ssum, f));
        if f>fmax:
            fmax = f;
            #print('fmax = {}'.format(fmax));
    fout.write('Case #{}: {}'.format(k+1, fmax));
    #print('Case #{}: {}'.format(k+1, fmax));
    if k+1<T:
        fout.write('\n');

fout.close();
del data;
fin.close();
