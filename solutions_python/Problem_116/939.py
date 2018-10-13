c_t = {'.': 0, 'X': 1, 'O': 2, 'T': 3}

def main():
    test_cnt = int(raw_input())
    for t in xrange(test_cnt):
        table = []
        end =False
        orig = []
        for i in xrange(4):
            line = raw_input()
            orig.append(line)
            table.append([c_t[e] for e in line])
        # check line by line
        for i, l in enumerate(table):
            if l[0] & l[1] & l[2] & l[3]:
                print 'Case #%d: %s won' % (t + 1, orig[i][0] == 'T' and orig[i][1] or orig[i][0])
                end = True
                break
        if end: raw_input(); continue

        # check column
        for i in xrange(4):
            if table[0][i] & table[1][i] &table[2][i] &table[3][i]:
                print 'Case #%d: %s won' % (t + 1, orig[0][i] == 'T' and orig[1][i] or orig[0][i])
                end = True
                break
        if end: raw_input(); continue

        if table[0][0] & table[1][1] & table[2][2] & table[3][3]: 
            print 'Case #%d: %s won' % (t + 1, orig[0][0] == 'T' and  orig[1][1] or orig[0][0])
            raw_input()
            continue

        if table[3][0] & table[2][1] & table[1][2] & table[0][3]: 
            print 'Case #%d: %s won' % (t + 1, orig[3][0] == 'T' and  orig[2][1] or orig[3][0])
            raw_input()
            continue

        # empty
        for l in orig:
            if '.' in l:
                print 'Case #%d: Game has not completed' % (t + 1,)
                end = True
                break
        if end: raw_input(); continue
        
        print 'Case #%d: Draw' % (t + 1,)
        raw_input()

if __name__ == '__main__':
    main()
