fin = open('A-large.in', 'r')
fout = open('A-large.out', 'w')


t = int(fin.readline())
for i in range(t):
    n, k = [int(a) for a in fin.readline().strip().split(' ')]

    if k % 2**n == 2**n -1:
        state = 'ON'
    else:
        state = 'OFF'
    print('Case #', i+1, ': ', state, sep='', file=fout)

fin.close()
fout.close()
