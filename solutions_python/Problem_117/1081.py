def main():
    T = int(raw_input())
    res = []
    for i in xrange(T):
        N,M = map(int,raw_input().split())
        lawn_mat = []
        for j in xrange(N):
            row_j = map(int, raw_input().split())
            lawn_mat.append(row_j)
        res_lawn = check_adj(lawn_mat)
        res.append(res_lawn)
    for i in xrange(1,T+1):
        print "Case #%d:"%i,res[i-1]

def check_adj(lawn_mat):
    N = len(lawn_mat)
    M = len(lawn_mat[0])
    trans_lawn = zip(*lawn_mat)
    for i in xrange(N):
        for j in xrange(M):
            #print lawn_mat[i][j], max(lawn_mat[i]), max(trans_lawn[j])
            if lawn_mat[i][j] != max(lawn_mat[i]) and lawn_mat[i][j] != max(trans_lawn[j]):
                return "NO"

    return "YES"        
            
                
if __name__ == "__main__":
    main()
