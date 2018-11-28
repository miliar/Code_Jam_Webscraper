import sys
n = sys.stdin.readline()
temp = int(n)

for i in range(temp):
    list=[]
    count = 0
    n = sys.stdin.readline()
    x=n.partition(' ')
    m=int(x[0])
    o=int(x[2])
    for j in range(m):
        n=sys.stdin.readline()
        n=n.rstrip('\n')
        list.append(n)
        x=n.rpartition('/')
        while x[0]:
            list.append(x[0])
            x=x[0].rpartition('/')
    set1=set(list)
    for j in range(o):
        n=sys.stdin.readline()
        n=n.rstrip('\n')
        if n in set1:
            continue
        count=count+1
        list.append(n)
        set1=set(list)
        x=n.rpartition('/')
        while x[0]:
            if not(x[0] in set1):
                count=count+1
                list.append(x[0])
                set1=set(list)
                x=x[0].rpartition('/')
            else:
                break
    print 'Case #%d: %d' %(i+1,count)
