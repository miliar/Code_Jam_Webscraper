f = open('A-large.in')
outf = open('result.txt','w')

def makeBase(c):
    d = {}
    for x in c:
        d[x] = -1

    base = len(d)

    if base == 1:
        base = 2
        
    return d, base

def getMin(dic, base, cyper):
    dic[cyper[0]] = 1

    n = 0
    for x in cyper[1:]:
        if dic[x] == -1:
            dic[x] = n
        else:
            continue
        
        if n == 0:
            n = 2
        else:
            n = n + 1

    cyperlist = [ x for x in cyper ]
    cyperlist.reverse()

    result = 0
    curr = 1
    for x in cyperlist:
        result = result + dic[x]*curr
        curr = curr*base

    return result
            

def main():
    nCase = int(f.readline())

    for x in range(nCase):
        outf.write('Case #'+str(int(x+1))+': ')
        cyper = f.readline().rstrip()

        symdic, base = makeBase(cyper)

        outf.write(str(getMin(symdic, base, cyper))+'\n')
        
if __name__ == '__main__':
    main()
    f.close()
    outf.close()
