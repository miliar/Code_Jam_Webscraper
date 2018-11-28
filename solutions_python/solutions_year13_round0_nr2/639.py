import sys
sys.stdin = open('B-small-attempt0.in', 'r')
sys.stdout = open('B-small-attempt0.out', 'w')
out = sys.stdout
N = input()
for i in range(1, N+1):
    out.write('Case #')
    out.write(str(i))
    out.write(': ')

    (N, M) = raw_input().split(' ')
    N = int(N)
    M = int(M)
    
    lawn = []
    for i in range(0, N):
        strip = raw_input().split(' ')
        if '2' not in strip:
            strip = ['0' if x == '1' else x for x in strip]
        lawn.append(strip)
    lawn = zip(*lawn)
    for i in range(0, M):
        strip = lawn[i]
        if '2' not in strip:
            strip = ['0' if x == '1' else x for x in strip]
        lawn[i] = ' '.join(strip)
    lawn = ' '.join(lawn)
    if '1' in lawn:
        print 'NO'
    else:
        print 'YES'

sys.stdin.close()
sys.stdout.close()
