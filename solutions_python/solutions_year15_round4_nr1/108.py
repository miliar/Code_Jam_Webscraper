import sys

def logger(f) :
    def wrapper(*args) :
        printerr('call '+ f.__name__+':', *args)
        ans = f(*args)
        printerr('ret  '+ f.__name__+':', ans)
        return ans
    return wrapper

def prework(argv):
    '''do something according to argv,
    return a message describing what have been done.'''
    
    return "nothing"

def readline(fun) : 
    return [fun(_) for _ in input().split()]
    
dire = {'>':(0,1), '<':(0,-1), '^':(-1,0), 'v':(1,0)}
def once():
    '''to cope once'''
    r,c = readline(int)
    m = [input() for _ in range(r)]
    #printerr(m)
    #@logger
    def has_arrow(i, j, d) :
        di, dj = d
        i += di
        j += dj
        while i>=0 and i<r and j>=0 and j<c :
            if m[i][j] != '.' :
                return True
            i += di
            j += dj
        return False
    def check() :
        cnt = 0
        for i in range(r) :
            for j in range(c) :
                #printerr(i, j, cnt)
                if m[i][j] == '.' :
                    continue
                d = dire[m[i][j]]
                if has_arrow(i,j,d) :
                    continue
                if any([has_arrow(i,j,dd) for dd in dire.values() if dd != d]) :
                    cnt += 1
                    continue
                return None
        return cnt
    ans = check() 
    return ans if ans != None else 'IMPOSSIBLE'

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
