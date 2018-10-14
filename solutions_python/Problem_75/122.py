#!/usr/bin/python
# coding: utf-8

class OpposedElementsFound(Exception) :
    pass

def main() :
    T = int(raw_input())
    for t in xrange(T) :
        args = raw_input().split()
        args.reverse()
        C = int(args.pop())
        allComb = {}
        for i in xrange(C) :
            s = args.pop()
            allComb[(s[0], s[1])] = s[2]
            allComb[(s[1], s[0])] = s[2]
        allOpposed = set()
        D = int(args.pop())
        for i in xrange(D) :
            s = args.pop()
            allOpposed.add( (s[0], s[1]) )
            allOpposed.add( (s[1], s[0]) )
        N = int(args.pop())
        S = args.pop()
        stack = []
        for i in S :
            stack.append(i)
            while len(stack) >= 2 :
                p = (stack[-1], stack[-2])
                if p in allComb :
                    stack.pop()
                    stack.pop()
                    stack.append(allComb[p])
                else :
                    break
            try :
                for j in xrange(len(stack)) :
                    for k in xrange(j, len(stack)) :
                        p = (stack[j], stack[k])
                        if p in allOpposed :
                            raise OpposedElementsFound()
            except OpposedElementsFound :
                stack[:] = []
        print 'Case #%d: [%s]' % ((t + 1), ', '.join(stack))

if __name__ == '__main__' :
    main()


