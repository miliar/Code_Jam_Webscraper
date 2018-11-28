import sys
fin = open('A-large.in','r')
sys.stdout = open('A-large.out','w')
T = int(fin.readline())
for cs in range(1,T+1):
    N,K = [int(x) for x in fin.readline().split(' ')]
    print('Case #%d: '%cs,end = '')
    if(K%(2**N) == 2**N-1): print('ON')
    else: print('OFF')
fin.close()
