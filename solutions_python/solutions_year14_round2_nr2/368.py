def solve(A,B,K):
    count = 0
    for i in range(A):
        for j in range(B):
            if i&j < K:
                count += 1
    return count

if __name__=="__main__":
    T = int(raw_input())
    for i in range(1,T+1):
        A,B,K = map(int, raw_input().split())
        print "Case #%d: %d" % (i, solve(A,B,K))
