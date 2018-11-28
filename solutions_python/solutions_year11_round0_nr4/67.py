import sys
from fractions import Fraction

fact =[0 for i in range(1001)]
fact[0]=1
for i in range(1,1001):
    fact[i]=i*fact[i-1]

P=[[0 for j in range(1001)] for i in range(1001)]
for n in range(1,1001):
    s=0;
    for k in range(1,n+1):
        if n == k:
            P[n][k]=1
        else:
            P[n][k]=fact[n]//fact[k]//fact[n-k]*P[n-k][0]
        s+=P[n][k]
    P[n][0]=fact[n]-s

E=[0 for i in range(1001)]

for n in range(1,1001):
    s=0
    for i in range(1,n+1):
        s+=P[n][i]/fact[n]*(E[n-i]+1)
    E[n]=(s + P[n][0]/fact[n])/(1 - P[n][0]/fact[n])

T = int(input())
for t in range(1,T+1):
    N=int(input())
    k=0
    line=[int(c) for c in input().split()]
    for n in range(0,N):
        if line[n]!=n+1:
            k+=1
    print('Case #{0}: {1}'.format(t,E[k]))
