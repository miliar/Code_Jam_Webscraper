'''
- Please follow my setup to not incur in any incompatibility

- Tested on a Windows XP OS
- x86 processor, NOT 64 bit

- Runs on CPython 2.5.x

- It's easier to use my setup:
    * Python Installer 2.5.4 for windows x86
    http://www.python.org/ftp/python/2.5.4/python-2.5.4.msi
    (taken from http://www.python.org/download/releases/2.5.4/)

- Needs gmpy module
    * GMPY Module, version 1.11 for windows, python 2.5
    http://gmpy.googlecode.com/files/gmpy-1.11.win32-py2.5.exe
    (taken from http://code.google.com/p/gmpy/downloads/list)

- Can take advantage of psyco to speedup execution so please install psyco module
    * PSYCO Module, version 1.6 for windows, python 2.5
    http://sourceforge.net/projects/psyco/files/psyco/1.6/psyco-1.6.win32-py25.exe/download
    (taken from http://psyco.sourceforge.net/)
'''

from gmpy import mpz

def main():
    
    dataset = open('C-small-attempt0.in') #C-small.in
    
    T = int(dataset.readline())
    for Ti in xrange(1, T+1):
    
        R, k = map(mpz, dataset.readline().split()[:-1])
        g = map(mpz, dataset.readline().split())

        #print 'R:', R, 'k:', k, 'g:', ','.join(map(str,g))
        
        euros = mpz(0)
        
        Ri = mpz(0)
        while Ri<R:
                        
            onboard = mpz(0)
            waiting = g[:]
            boarding = []
            
            for i,gi in enumerate(g):
                onboard2 = onboard+gi
                if onboard2<=k:
                    boarding.append(waiting.pop(0))
                    onboard = onboard2
                else:
                    break
            
            euros += onboard
            g = waiting + boarding
            
            Ri += 1
            
        print 'Case #%d: %d' % (Ti, euros)
    
    dataset.close()
    
def timetest():
    from timeit import Timer
    t = Timer("main()")
    print t.timeit(10)

if __name__=='__main__':
    try:
        import psyco
        psyco.full()
    except ImportError:
        pass
    main()
