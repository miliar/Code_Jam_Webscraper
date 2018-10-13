#!/usr/bin/env python
def flip(pc, K):
    pc = list(pc)
    counter = 0
    for i in range(len(pc)):
        if pc[i] == '-' and i + K < len(pc)+1:
            for j in range(i, i+K):
                pc[j] = '+' if pc[j] == '-' else '-'
            counter += 1
    return (counter, pc.count('+') == len(pc))
    
for T in range(1, int(input())+1):
    pancake, K = input().split()
    K = int(K)
    res = flip(pancake, K)
    o = res[0] if res[1] else 'IMPOSSIBLE'
    print('Case #{}: {}'.format(T, o))