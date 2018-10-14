#!/usr/bin/env python

def int_list(s):
    return map(lambda x: int(x), s.split())

def main():
    cases = int(raw_input())
    for case in xrange(cases):
        line = int_list(raw_input())
        L, t, N, C = line[0], line[1], line[2], line[3]
        a = line[4:]

        ind = 0
        for i in xrange(C, N):
            a.append(a[ind])
            ind = (ind + 1) % C
        
        hours = 0
        others = []
        for i in xrange(N):
            if hours > t:
                others = [(hours - t) / 2] + a[i:]
                hours -= (hours - t)
                break
            elif hours == t:
                others = a[i:]
                break
            else:
                hours += a[i] * 2
        
        others = reversed(sorted(others))
        for i in others:
            if L > 0:
                hours += i
                L -= 1
            else:
                hours += i * 2
        
        print 'Case #%d: %d' % (case + 1, hours)
    
if __name__ == '__main__':
    main()