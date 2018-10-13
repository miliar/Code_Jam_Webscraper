#Python3

def check_row(lawn, N, M, n, m):
    h = lawn[n][m]
    for i in range(M):
        if lawn[n][i] > h:
            return False
    return True

def check_column(lawn, N, M, n, m):
    h = lawn[n][m]
    for j in range(N):
        if lawn[j][m] > h:
            return False
    return True


T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    lawn = []
    for n in range(N):
        lawn.append(list(map(int, input().split())))
        if len(lawn[-1]) != M:
            raise RuntimeError
    
    yesno = True
    for n in range(N):
        for m in range(M):
            if not (check_row(lawn, N, M, n, m) or check_column(lawn, N, M, n, m)):
                yesno = False
                break
        if not yesno:
            break
        
    if yesno:
        print("Case #%d: YES" % (t+1))
    else:
        print("Case #%d: NO" % (t+1))
    


