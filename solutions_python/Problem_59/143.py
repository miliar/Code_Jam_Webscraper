import sys

def addpathlist(l,path):
    count = 0
    dirs = path.split("/")
    for i in xrange(len(dirs)):
        p = ("/").join(dirs[:i+1])
        if p not in l:
            l.append(p)
#            print p
            count += 1
    return count

def calcMkdir(a,c):
    a.split()

def readinput(fname):
    n,m,num = 0,0,0
    for i,line in enumerate(open(fname)):
        if i == 0:
            t = line.strip().split()[0]
            continue
        elif n < 1 and m<1:
            n,m = [int(x) for x in line.strip().split()]
            a,c =[],0
#            print n,m
            num += 1
        elif n >= 1:
            addpathlist(a,line.strip()[1:])
            n -= 1
        elif m >= 1:
            c += addpathlist(a,line.strip()[1:])
            m -= 1
            if m < 1:
                print "Case #%d: %d"%(num,c)

def main():
    readinput(sys.argv[1])

if __name__ == '__main__':
    main()