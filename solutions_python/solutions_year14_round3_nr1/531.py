file=open('c:/CODEJAM/A-large.in')

## Number of Cases
T=int(file.next().rstrip('\n'))

for t in range(T):

    PQ=file.next().split('/')
    PQ=map(float,PQ)
    P=PQ[0]
    Q=PQ[1]

    for g in range(1,42):
        if ((P/Q)%(1.0/2**(g))==0):     
            break

    if g>40:
        print('Case #{}: {}'.format(t+1,'IMPOSSIBLE'))
    elif (P/Q > (1.0/2**(g))):
         for g2 in range(1,g):
            if (P/Q>(1.0/2**(g2))):
                print('Case #{}: {}'.format(t+1,g2))
                break
    else:
        print('Case #{}: {}'.format(t+1,g))
