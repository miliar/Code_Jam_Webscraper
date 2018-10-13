def solve():
    M,S = input().split()
    M=int(M)
    S=[int(s) for s in S]

    c=0
    e=0
    for k in range(M+1):
        if(c<k):
            e = e+1
            c = c+1
        c = c+S[k]

    return e

if __name__ == '__main__':
    T = int(input())

    for t in range(1,T+1):
        print("Case #%d: %d" % (t,solve()))
