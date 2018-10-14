'''
Created on 2010-5-8

@author: Zhonghao
'''

def full(k, G):
    money = 0
    for i in range(len(G)):
        if money + G[i] > k:
            return i, money
        
        money += G[i]
        
    
def count_money(R, k, G):
    if sum(G) <= k:
        return R * sum(G)
    
    loc = []
    money = []
    for i in range(len(G)):
        tmp = G[i:]
        tmp.extend(G[:i])
        loc_, money_ = full(k, tmp)
        loc_ = (loc_ + i) % len(G)
        loc.append(loc_)
        money.append(money_)
        
    print loc
    loc_set = set()
    seq = []
    money_small = 0
    
    last = 0
    while R > 0:
        money_small += money[last]
        loc_set.add(last)
        seq.append(last)
        R -= 1
        #if loc[last] in loc_set:
            #print seq
        #    break
        last = loc[last]
    
    print seq
    
    if R == 0:
        return money_small
    
    money_sum = money_small
    start = None
    for i in range(len(seq)):
        if seq[i] == loc[seq[-1]]:
            start = i
    
    seq = seq[start:]
    money_rep = 0
    for i in seq:
        money_rep += money[i]
    
    times = R / len(seq)
    money_sum += times * money_rep    
    rest = R % len(loc_set)
    
    while rest > 0:
        money_sum += money[last]
        last = loc[last]
        rest -= 1
    
    print 'hi'    
    return money_sum
        

if __name__ == '__main__':
    import sys
    in_file = sys.argv[1]
    out_file = sys.argv[2]
    
    lines = open(in_file).readlines()
    lines = [x.rstrip() for x in lines]
    lines = lines[1:]
    
    case_no = 0
    wfile = open(out_file, 'w')
    while lines:
        l1 = lines[0]
        l2 = lines[1]
        lines = lines[2:]
        R, k, g = l1.split()
        R = int(R)
        k = int(k)
        g = int(g)
        G = l2.split()
        G = [int(x) for x in G]
        case_no += 1
        wfile.write('Case #' + str(case_no) + ': ')
        #print R, k, G
        money = count_money(R, k, G)
        wfile.write(str(money) + '\n')
        
    
    
    
    
    
        
# END      