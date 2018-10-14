import sys

def addwire(ws,(a,b)):
    addins = 0
    for (x,y) in ws:
        if a-x > 0 and b-y < 0:
            addins += 1
        elif a-x < 0 and b-y > 0:
            addins += 1
    ws.append((a,b))
    return addins

def readinput(fname):
    count,num = 0,0
    for i,line in enumerate(open(fname)):
        if i == 0:
            t = line.strip().split()[0]
            continue
        elif count < 1:
            n = int(line.strip())
            ws,ins = [],0
            num += 1
            count= n
        else:
            a,b = [int(x) for x in line.strip().split()]
            ins += addwire(ws,(a,b))
            count -= 1
            if count < 1:
                print "Case #%d: %d"%(num,ins)

def main():
    readinput(sys.argv[1])

if __name__ == '__main__':
    main()