#! /opt/local/bin/python
# -*- coding: utf8 -*-


def main():
    for case in range(input()):
        p, k, l = map(int, raw_input().split())
        freq = map(int, raw_input().split())

        freq.sort(reverse=True)

        if ( p * k ) < l:
            print 'Case #%d: Impossible' % ( case+1 )

        else:
            count = 0
            push = []
            for i in range(p):
                for j in range(k):
                    push.append(i+1)
        
            for i in range(l):
                count += push[i] * freq[i]
            
            print 'Case #%d: %d' % ( case+1, count )

if __name__ == '__main__':
    main()

