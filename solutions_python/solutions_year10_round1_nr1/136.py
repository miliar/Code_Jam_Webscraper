#!/usr/bin/env python

def solve(t):
    n, G = map(lambda x: int(x), raw_input().split())
    d = []
    ans = 'Neither'
    for i in xrange(n):
        a = raw_input().strip()
        a = list(a)
        j = n - 1
        while j > 0:
            if ''.join(a[0:j]) == '.'*j:
                break
                
            if a[j] == '.':
                for k in xrange(j, 0, -1):
                    a[k] = a[k-1]
                a[0] = '.'
                if a[j] != '.':
                    j -= 1
            else:
                j -= 1
        a = ''.join(a)
        d.append(a)
        
    r = []
    for j in xrange(n):
        a = []
        for i in xrange(n):
            a.append(d[i][j])
        a.reverse()
        r.append(''.join(a))

    win = [0, 0]    
    for i in xrange(n-1, -1, -1):
        for j in xrange(n):
            bcount = [0, 0, 0, 0]
            rcount = [0, 0, 0, 0]

            # count 1
            turn = 0
            for k in xrange(i, i - G - 1, -1):
                if k < 0:
                    break
                if r[k][j] == 'R':
                    if turn == 0:
                        rcount[0] += 1
                    else:
                        rcount[0] = 1
                        turn = 0
                elif r[k][j] == 'B':
                    if turn != 1:
                        bcount[0] = 1
                        turn = 1
                    else:
                        bcount[0] += 1
                else:
                    turn = 2
                    
            # count 2
            turn = 0
            for k in xrange(j, j + G + 1):
                if k == n:
                    break
                if r[i][k] == 'R':
                    if turn == 0:
                        rcount[1] += 1
                    else:
                        rcount[1] = 0
                        turn = 0
                elif r[i][k] == 'B':
                    if turn != 1:
                        bcount[1] = 1
                        turn = 1
                    else:
                        bcount[1] += 1
                else:
                    turn = 2
                    
            # count 3
            l = j
            turn = 0
            for k in xrange(i, i - G - 1, -1):
                if k < 0 or l == n:
                    break
                if r[k][l] == 'R':
                    if turn == 0:
                        rcount[2] += 1
                    else:
                        rcount[2] = 1
                        turn = 0
                elif r[k][l] == 'B':
                    if turn != 1:
                        bcount[2] = 1
                        turn = 1
                    else:
                        bcount[2] += 1
                else:
                    turn = 2
                l += 1
                
            # count 4
            l = j
            turn = 0
            for k in xrange(i, i - G - 1, -1):
                if k < 0 or l < 0:
                    break
                if r[k][l] == 'R':
                    if turn == 0:
                        rcount[3] += 1
                    else:
                        rcount[3] = 1
                        turn = 0
                elif r[k][l] == 'B':
                    if turn != 1:
                        bcount[3] = 1
                        turn = 1
                    else:
                        bcount[3] += 1
                else:
                    turn = 2

                l -= 1
            
            for k in rcount:
                if k == G:
                    win[0] = 1
                    break
                    
            for k in bcount:
                if k == G:
                    win[1] = 1
                    break

    result = ''.join(map(lambda x: str(x), win))
    if result == '00':
        ans = 'Neither'
    elif result == '10':
        ans = 'Red'
    elif result == '01':
        ans = 'Blue'
    else:
        ans = 'Both'
    print 'Case #%d: %s' % (t, ans)

def main():
    cases = int(raw_input())
    for case in xrange(1, cases + 1):
        solve(case)
    
if __name__ == '__main__':
    main()