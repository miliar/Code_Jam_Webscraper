#!/usr/bin/env python

def int_list(s):
    return map(lambda x: int(x), s.split())

def main():
    cases = int(raw_input())
    for case in xrange(cases):
        row, col = int_list(raw_input())
        m = []
        for i in xrange(row):
            m.append(list(raw_input()))
        
        for r in xrange(row):
            for c in xrange(col):
                if m[r][c] == '#':
                    if c + 1 < col and r + 1 < row:
                        m[r][c] = '/'
                        m[r][c+1] = "\\"
                        m[r+1][c] = '\\'
                        m[r+1][c+1] = '/'
                    else:
                        m[r][c] = 'u'

        NO = False
        for r in xrange(row):
            for c in xrange(col):
                if m[r][c] == '#' or m[r][c] == 'u':
                    NO = True
                    break
        
        print 'Case #%d:' % (case + 1)
        if NO:
            print 'Impossible'
        else:
            
            for r in xrange(row):
                print ''.join(m[r])
    
if __name__ == '__main__':
    main()