import sys

def swap01(x):
    if x == 1:
        return 0
    elif x == 0:
        return 1
    else:
        return x

def cutboard(i,j,size,ban):
    if ban[i][j] == -1:
        return False
    for x in xrange(size):
        for y in xrange(size):
            if ban [i+x][j+y] == -1:
                return False
            elif (x+y) % 2 == 0 and ban [i+x][j+y] == ban [i][j]:
                continue
            elif (x+y) % 2 == 0 and ban [i+x][j+y] != ban [i][j]:
                return False
            elif (x+y) % 2 == 1 and swap01(ban [i+x][j+y]) == ban [i][j]:
                continue
            elif (x+y) % 2 == 1 and ban [i+x][j+y] == ban [i][j]:
                return False
#    print size,i,j
    for x in xrange(size):
        for y in xrange(size):
            ban [i+x][j+y] = -1
    return True

def cutoutban(m,n,ban):
    detail = []
    maxsize = m
    if n < m:
        maxsize = n
    for size in range(maxsize,0,-1):
        count = 0
        for i in xrange(m - size +1):
            for j in xrange(n - size + 1):
                if cutboard(i,j,size,ban) == True:
                    count += 1
        if count != 0:
            detail.append([size,count])
    return detail

def csato2(s):
    return [int(s,16) / 8,(int(s,16)%8) / 4,(int(s,16)%4) / 2,int(s,16) % 2]

def readinput(fname):
    count,num = 0,0
    for i,line in enumerate(open(fname)):
        if i == 0:
            t = line.strip().split()[0]
            continue
        elif count < 1:
            m,n = [int(x) for x in line.strip().split()]
            num += 1
            ban = []
            count= m
        else:
            rs = []
            for s in line.strip():
                rs += csato2(s)
            ban.append(rs)
            count -= 1
            if count < 1:
#                print ban
                detail = cutoutban(m,n,ban)
                print "Case #%d: %d"%(num,len(detail))
                for size,cnt in detail:
                    print size,cnt

def main():
    readinput(sys.argv[1])

if __name__ == '__main__':
    main()