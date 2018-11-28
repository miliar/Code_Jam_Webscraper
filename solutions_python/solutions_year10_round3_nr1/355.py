import os, sys

def intersect(a, b):
    if (a[0]-b[0]<0 and a[1]-b[1]>0) or (a[0]-b[0]>0 and a[1]-b[1]<0):
        return True
    else:
        return False


def checkall(L):
    i = 0
    for elem in L:
        for E in L:
            if intersect(elem, E):
                i += 1
        L.pop(0)
    return i

def getList(LL):
    ll = []
    for l in LL:
        ll.append([int(i) for i in l[:-1].split(' ')])
    return ll

def parse(fName):
    h = open(fName, 'r')
    w = open(os.path.join(os.path.split(fName)[0], os.path.split(fName)[1][:-3]+'.out'), 'w')
    lines = h.readlines()
    lines.pop(0)
    k = 0
    case = 0
    for line in lines:
        if len(line[:-1])==1:
            case += 1
            L = getList(lines[k+1:k+int(line[:-1])+1])
            print L
            pts = checkall(L)
            w.write('Case #'+str(case)+': '+str(pts)+'\n')
        k += 1
    h.close()
    w.close()

if __name__ == '__main__':
    parse(sys.argv[1]) 
