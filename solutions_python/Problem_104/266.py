from optparse import OptionParser
from itertools import combinations

class Test:
    def __init__(self, fd):
        data = map(int, fd.readline().strip().split())
        self.N = data[0]
        self.s = data[1:self.N+1]
        self.s.sort()
                 
    def run(self):
        for i in range(2,self.N):
            for c in combinations(range(self.N-1), i):
                s1 = map(lambda x: self.s[x], c)
                s2 = []
                S = sum(s1)
                for j in range(self.N):
                    if self.s[j] not in s1:
                        if (sum(s2)+self.s[j] > S):
                            break
                        s2.append(self.s[j])
                        if (sum(s2) == S):
                            return [s1,s2]
                        
        return None
    

def main():
    parser = OptionParser()
    args = parser.parse_args()[1]
    ifile = './sources/' + args[0]+'-'+args[1]+'-'+args[2]+'.in'
    ofile = './sources/' + args[0]+'-'+args[1]+'-'+args[2]+'.out'
    print 'Loading data from ', ifile
    ifd = open(ifile, 'r')
    ofd = open(ofile, 'w')
    
    for t in range(1, int(ifd.readline().strip())+1):
        R = Test(ifd).run()
        ofd.write('Case #{0}: \n'.format(t))
        print 'Case #{0}: '.format(t)
        if R is None:
            ofd.write('Imposible\n')
            print 'Imposible'
        else:
            print ' '.join(map(str,R[0]))
            print ' '.join(map(str,R[1]))
            ofd.write(' '.join(map(str,R[0]))+'\n')
            ofd.write(' '.join(map(str,R[1]))+'\n')
    
    ofd.close()
    
if __name__ == '__main__':
    main()