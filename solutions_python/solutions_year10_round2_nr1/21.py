'''
Created on 22 May 2010

@author: Shahar
'''

def A(inpfile):
    fin = open(inpfile, 'r')
    fout = open(inpfile+'.out', 'w')
    CNT = int(fin.readline())
    for iCNT in xrange(CNT):
        numbers = map(int, fin.readline().rstrip('\n').split(' '))
        N = numbers[0]
        M = numbers[1]
        Root = {};
        for iN in xrange(N) :
            FullPath = fin.readline().rstrip('\n').lstrip('/')
            Dirs = FullPath.split('/')
            CurrDir = Root;
            for Dir in Dirs:
                if Dir not in CurrDir :
                    CurrDir[Dir] = {}
                CurrDir = CurrDir[Dir]
        MkDirs = 0
        for iM in xrange(M) :
            FullPath = fin.readline().rstrip('\n').lstrip('/')
            Dirs = FullPath.split('/')
            CurrDir = Root;
            for Dir in Dirs:
                if Dir not in CurrDir :
                    MkDirs += 1 
                    CurrDir[Dir] = {}
                CurrDir = CurrDir[Dir]
                    
        text = 'Case #' + str(iCNT+1) + ': ' + str(MkDirs)
        print text
        fout.write(text + '\n')

if __name__ == "__main__":
    #A(sys.argv[1]);
    #A('..\\test\\A-test.in');
    #A('..\\test\\A-small-attempt0.in');
    #A('..\\test\\A-small-attempt1.in');
    A('..\\test\\A-large.in');
