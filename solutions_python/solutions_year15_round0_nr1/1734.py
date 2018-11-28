#!/usr/bin/python
def solve():
    T = int(raw_input())
    for t in xrange(1,T+1):
        S,k = raw_input().split()
        if int(S) > 0 :
            au,fr,df= int(k[0]),0,0
            for i in xrange(1,len(k)):
                if(k[i] != '0'):
                    df = i-(au+fr)
                    if df > 0 : fr = fr + df
                    au = au + int(k[i])
        else : fr = 0
        print 'Case #{}: {}'.format(t,fr)

if __name__ == "__main__":
    solve()

