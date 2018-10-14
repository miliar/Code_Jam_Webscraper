import sys

def prework(argv):
    '''do something according to argv,
    return a message describing what have been done.'''
    
    return "nothing"

def once():
    '''to cope once'''
    n, x = [int(_) for _ in input().split()]
    ss = [int(_) for _ in input().split()]
    ss.sort()
    cnt = 0
    while len(ss) > 1 :
        big = ss.pop()
        if ss[0] + big <= x :
            ss.pop(0)
        cnt += 1
    if len(ss) > 0 :
        cnt += 1
    return cnt

def printerr(*v):
    print(*v, file=sys.stderr)

def main():
    TT = int(input())
    for tt in range(1,TT+1):
        printerr("coping Case %d.."%(tt))
        ans = once()
        print("Case #%d: %s"%(tt, (ans)))

if __name__ == '__main__' :
    msg = prework(sys.argv)
    print("prework down with", msg, file=sys.stderr)
    main()
