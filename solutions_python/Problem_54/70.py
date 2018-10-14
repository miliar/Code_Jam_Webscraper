#!/usr/bin/env python

T = int(raw_input())

def mdc(x, y):
    if y == 0:
        return x
    else:
        return mdc(y, x%y)

for t in range(T):
    linha = raw_input().split()
    N = int(linha[0])
    tempo = map(int, linha[1:])
    menor = min(tempo)

    divisor = 0

    for n in tempo:
        divisor = mdc(divisor, n - menor)

    resp = (divisor - tempo[0] % divisor) % divisor

    print 'Case #%d: %d' %(t+1, resp)
