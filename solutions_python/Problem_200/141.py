#!/usr/bin/env python3


T = int(input())
for t in range(1,T+1):
    N = list(input())
    N2 = int(''.join(N))
#    print(N)
    candidates = list()
    radix = N.pop(0)
    if radix == '1':
        if len(N) == 0:
            candidates.append(int(radix))
        else:
            candidates.append(int('9'*len(N)))
    else:
        candidates.append(int(str(int(radix)-1) + '9'*len(N)))
    while N:
        #print(N, radix, candidates)
        current = N.pop(0)
        if current > radix[-1]:
            tmp = radix + str(int(current)-1) + '9'*len(N)
            candidates.append(int(tmp))
            radix += current
        elif current == radix[-1]:
            radix += current
        elif current < radix[-1]:
            radix = '0'
        else:
            raise Exception("This should not happen!")
    candidates.append(int(''.join(radix)))
    #print(candidates)
    
    print('Case #%d: %d'%(t,max(candidates)))
       
