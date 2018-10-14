from math import ceil

__author__ = 'firefly'


fin = open('input.txt','rt')
fout = open('output.txt','wt')

fin.readline()

index = 1
for line in fin:
    symbols = line.split(' ')

    N = int(symbols.pop(0))
    S = int(symbols.pop(0))
    p = int(symbols.pop(0))

    total_points = [int(x) for x in symbols]

    total_points.sort()
    total_points.reverse()

    count = 0
    while len(total_points)>0 and ceil(total_points[0]/3.) >= p:
        total_points.pop(0)
        count+=1

    while(len(total_points)>0 and S>0):
        val = ceil(total_points[0]/3.)
        if(total_points[0] > 0 and total_points[0]%3==0 or total_points[0]%3==2):
            val+=1

        if(val >= p):
            count+=1
        else:
            break
        total_points.pop(0)
        S-=1

    print('Case #{0}: {1}'.format(index, count),file=fout)
    index+=1

fout.close()