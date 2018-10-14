"""
Created on May 7, 2010

@author: oren
"""

def parseFile(instr, outstr):
    fin = open(instr)
    fout = open(outstr,'w')
    cases = int(fin.next())
    for casenum in xrange(1,cases+1):
        n,k = map(int,fin.next().split())
        ans = compute(n,k)
        output(fout,casenum,ans)
    fout.flush()
    fout.close()
    fin.close()

def compute(n,k):
    m = 2**n
    return 'ON' if k%m == m-1 else 'OFF'

def output(fout,casenum,ans):
    s = 'Case #%d: %s' % (casenum,ans)
    print s
    fout.write(s + '\n')

if __name__ == '__main__':
    #parseFile('snapper-test.in','snapper-test.out')
    #parseFile('A-small-attempt0.in','A-small.out')
    parseFile('A-large.in','A-large.out')