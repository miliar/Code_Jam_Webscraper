from __future__ import print_function

def strategy_war(b1, b2):
    count = 0
    while(len(b1)):
        if b1.pop() > b2[-1]:
            count+=1
            b2.pop(0)
        else:
            b2.pop()
    return count

def strategy_war2(b1, b2):
    count = 0
    while(len(b1)):
        if b1[-1] > b2.pop():
            count+=1
            b1.pop()
        else:
            b1.pop(0)
    return count

if __name__ == '__main__':
    n = int(raw_input())
    for pb_i in xrange(n):
        # Solve problem i
        nb_block = int(raw_input())
        blocks_naomi = [float(_) for _ in raw_input().split()]
        blocks_ken = [float(_) for _ in raw_input().split()]

        blocks_naomi.sort()
        blocks_ken.sort()

        result = [strategy_war2(list(blocks_naomi), list(blocks_ken)), strategy_war(list(blocks_naomi), list(blocks_ken))]
        
        
        print("Case #{}: {} {}".format(pb_i+1, result[0], result[1]))
