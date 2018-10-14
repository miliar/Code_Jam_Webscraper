import sys

def calcEuros(r,k,n,gs):
#    print r,k,n,gs
    Euros,dic = 0,{}
    for i in range(r):
#        print Euros,gs
        if tuple(gs) in dic.keys():
            Euros += dic[tuple(gs)][0]
            gs = dic[tuple(gs)][1]
            continue
        count = 0
        for c,j in enumerate(range(n)):
            count += gs[j]
            if count > k:
                Euros += sum(gs[:j])
                nextgs = gs[j:] + gs[:j]
                dic[tuple(gs)] = (sum(gs[:j]),nextgs)
                gs = nextgs
                break
            elif c == n-1:
                Euros += sum(gs)
                dic[tuple(gs)] = (sum(gs),gs)
    return Euros

def readinput(fname):
    count,num = 0,0
    for i,line in enumerate(open(fname)):
        if i == 0:
            t = line.strip().split()[0]
        elif count < 1:
            r,k,n = [int(x) for x in line.strip().split()]
#            print r,k,n
            count = 1
            num += 1
        else:
            gs = [int(x) for x in line.strip().split()]
#            print gs
            y = calcEuros(r,k,n,gs)
            print "Case #%d: %d"%(num,y)
            count -= 1

def main():
    readinput(sys.argv[1])

if __name__ == '__main__':
    main()