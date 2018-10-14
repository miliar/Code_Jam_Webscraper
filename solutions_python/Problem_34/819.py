#! /usr/bin/env python
#coding=utf-8

class Model:
    def __init__(self, mode):
        self.mode = mode
        self.starts = []
        quote = False
        first = False
        for j in xrange(len(self.mode)):
            c = self.mode[j]
            if c == '(':
                quote = True
                first = True
            elif c == ')':
                quote = False
            else:
                if quote == True:
                    if first == True:
                        self.starts.append(j)
                        first = False
                else:
                    self.starts.append(-j)        
        
    def match_one(self, s):
        for k in xrange(len(s)):
            c = s[k]
            start = self.starts[k]
            if start <= 0:
                m = self.mode[-start]
                if m != c:
                    return False
            else:
                for m in self.mode[start:]:
                    if m == c:
                        break
                    elif m == ')':
                        return False
        return True
    
    def matches(self, strs):
        count = 0
        for s in strs:
            if self.match_one(s):
                count += 1
        return count

def main():
    L, D, N = (int(x) for x in raw_input().strip().split())
    strs = []
    for i in xrange(D):
        strs.append(raw_input().strip())
    for i in xrange(N):
        model = Model(raw_input().strip())
        match = model.matches(strs)
        print 'Case #%d: %d' % (i+1, match)
        

if __name__ == '__main__':
    main()
