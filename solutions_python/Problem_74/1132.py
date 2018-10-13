#!/usr/bin/env python

def main():
    cases = input()
    for case in range(1, cases+1):
        ans = 0
        
        line = raw_input().split()[1:]
        wall = {'O': [], 'B': []}
        order = []
        for i in range(len(line) / 2):
            order.append(line[i*2])
            wall[line[i * 2].upper()].append(int(line[i * 2 + 1]))
        
        oi, bi = 0, 0
        ostand, bstand = 1, 1
        while True:
            ans += 1
            oc, bc = False, False
            olen, blen = len(wall['O']), len(wall['B'])
            
            if oi < olen:
                onext = wall['O'][oi]
            else:
                oc = True
                
            if bi < blen:
                bnext = wall['B'][bi]
            else:
                bc = True
            
            if not oc and ostand != onext:
                if ostand < onext:
                    ostand += 1
                elif ostand > onext:
                    ostand -= 1
                oc = True
                
            if not bc and bstand != bnext:
                if bstand < bnext:
                    bstand += 1
                elif bstand > bnext:
                    bstand -= 1
                bc = True
                        
            if not oc and order[0] == 'O':
                oi += 1
                order = order[1:]
                bc = True
                
            if not bc and order[0] == 'B':
                bi += 1
                order = order[1:]
                oc = True
            
            if bi >= blen and oi >= olen:
                break            
        
        print 'Case #%d: %d' % (case, ans)

if __name__ == '__main__':
    main()