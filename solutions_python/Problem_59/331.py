#Problem: File Fix-it

def readInt():return int(raw_input())
def readStr():return str(raw_input())
#def readArray(foo):return foo(raw_input().split())
def readArray(foo): return [foo(x) for x in raw_input().split()]

def parse2(existing, newly):
    dirs=[]
    for i in range(len(existing)):
        s=existing[i].split('/')
        for j in range(1, len(s)):
            r=''
            for x in range(j+1):
                r=r + '/'+s[x]
            dirs.append(r[1:])
    res=0
    for i in range(len(newly)):
        s=newly[i].split('/')
        for j in range(1, len(s)):
            r=''
            for x in range(j+1):
                r=r + '/'+s[x]
            if r[1:] not in dirs:
                res = res+1
                dirs.append(r[1:])
    return res   

cases=readInt()
for case in range(cases):
    (exist, new)=readArray(int)
    ex=[]
    ne=[]
    for i in range(exist):
        ex.append(readStr())

    for i in range(new):
        ne.append(readStr())

    print 'Case #%d: %d' % (case+1, parse2(ex,ne))
    
    
##print parse(['/chicken', '/chicken/egg'], ['/chicken'])
###should be 0
##print parse([], ['/home/gcj/finals', '/home/gcj/quals'])
##should be 4