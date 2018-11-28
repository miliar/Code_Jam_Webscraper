#!/usr/bin/env python3

def main():
    T = int(input())
    for t in range(1,T+1):
        nbA,nbB = map(int,input().split())
        A = []
        for _ in range(nbA):
            b,e = map(int,input().split())
            A.append((b,e,0))
        for _ in range(nbB):
            b,e = map(int,input().split())
            A.append((b,e,1))
        A.sort()
        cpt = 0
        X = [0,0]
        F = [[],[]]
        margin = 0
        curr,x = A[0][0],A[0][2]
        x0 = x
        for i in range(len(A)):
            b,e,y = A[i]
            if y==x:
                if b-curr>0:
                    F[x].append(b-curr)
                X[x] += e-curr
            else:
                cpt += 1
                x = y
                margin += b-curr
                X[x] += e-b
            curr = e
        if x0==x:
            d = A[0][0] + 24*60-A[-1][1]
            X[x] += d
            F[x].append(d)
        else:
            cpt += 1
            margin += A[0][0] + 24*60-A[-1][1]
        #print(X[0]+X[1]+margin)
        assert(X[0]+X[1]+margin==24*60)
        #print(margin,X,F)
        if X[0]>X[1]:
            X[0],X[1] = X[1],X[0]
            F[0],F[1] = F[1],F[0]
        if X[1]-margin>720:
            D = X[1]-720-margin
            #print(D)
            F[1].sort(reverse=True)
            i = 0
            while D>0:
                D -= min(D,F[1][i])
                cpt += 2
                i += 1
        print('Case #%d: %d' % (t,cpt))

main()
