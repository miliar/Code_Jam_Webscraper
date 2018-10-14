import sys

def build(C, F, X, G):
    elapsed = 0.0
    tm_min = X / G
    for i in xrange(int(X/C) + 1):
        tm_nb = elapsed + X / G
        if tm_nb < tm_min:
            tm_min = tm_nb
        elapsed += C / G
        G += F
    return tm_min

def solve(C, F, X):
    return build(C, F, X, 2.0)

def main():
    case_num = int(raw_input())
    for i in xrange(case_num):
        line = raw_input()
        row1 = int(line) - 1
        mx1 = []
        for j in xrange(4):
            line = raw_input()
            mx1.append(map(int, line.split(' ')))
        line = raw_input()
        row2 = int(line) - 1
        mx2 = []
        for j in xrange(4):
            line = raw_input()
            mx2.append(map(int, line.split(' ')))
        ans = set(mx1[row1]) & set(mx2[row2])
        #print mx1[row1]
        #print mx2[row2]
        if not ans:
            print 'Case #%d: %s' % (i+1, 'Volunteer cheated!')
        if len(ans) > 1:
            print 'Case #%d: %s' % (i+1, 'Bad magician!')
        else:
            for a in ans:
                print 'Case #%d: %d' % (i+1, a)
                
main()

