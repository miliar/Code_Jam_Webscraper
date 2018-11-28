#!/usr/bin/env python
class Welcome(object):
    def __init__(self,filename):
        self.num = None
        self.tests = []
        self.target = 'welcome to code jam'

        with open(filename) as f:
            for line in f.readlines():
                line = line.strip()
                if not self.num:
                    self.num = int(line)
                else:
                    self.tests.append(line)
                    
    def solve(self):
        i=0
        for test in self.tests:
            i+=1
                
            count = self.count(test)
            count = count % 1000
            print "Case #%s: %04d" % (i,count)
        
    def count(self,s,idx=0,tally=None):
        if tally is None:
            tally = ''
        elif tally == self.target:
            return 1

        count = 0
        for pos in xrange(len(s)):
            if s[pos] == self.target[idx]:
                new_tally = tally+s[pos]
                count += self.count(s[pos+1:],idx+1,new_tally)

        return count
        
if __name__ == '__main__':
    import sys
    Welcome(sys.argv[1]).solve()