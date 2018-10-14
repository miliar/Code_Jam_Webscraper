#!/usr/bin/env python3

def main():
    T = int(input())
    for t in range(1,T+1):
        N,R,_,Y,_,B,_ = map(int,input().split())
        X = sorted([(R,'R'),(Y,'Y'),(B,'B')],reverse=True)
        S = [0,1]*X[1][0]+[0]*(X[0][0]-X[1][0])
        k = len(S)-1
        for i in range(X[2][0]):
            if S[k]!=2 and (k+1==len(S) or S[k+1]!=2):
                S = S[:k+1]+[2]+S[k+1:] if k+1<len(S) else S[:k+1]+[2]
            k -= 1
        if S[0]!=S[-1] and all(S[i]!=S[i+1] for i in range(len(S)-1)):
            R = [X[S[i]][1] for i in range(len(S))]
            print('Case #%d: %s' % (t,''.join(R)))
        else:
            print('Case #%d: IMPOSSIBLE' % (t))

main()
