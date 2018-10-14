import sys
import re
from gmpy import mpz
input=sys.stdin

def N():
    N='0'
    while True:
        yield N
        if N=='9':
            N='a'
        else:
            N=chr(ord(N)+1)
            if N=='1':
                N='2'

def rebase(x):
    if ord(x) in range(ord('0'),ord('9')+1):
        return int(x)
    else:
        return 10+(ord(x)-ord('a'))

def count(n):
    digs=[x for x in n]
    udigs={}
    for x in digs:
        if x not in udigs:
            udigs[x]=None
    udigs[digs[0]]='1'
    n=N()
    for x in digs:
        if udigs[x] is None:
            udigs[x]=n.next()
    dig=''.join([udigs[x] for x in digs])
    mbase=rebase(max(udigs.values()))
    a=mpz(dig,mbase+1)
    return a
    # print '----',a
    # print mbase
    # print udigs
    # print digs
    # print dig

T=int(input.readline())
for i in xrange(1,T+1):
    n=re.sub('\n','',input.readline())
    n=count(n)
    print "Case #%s: %s" % (i,n)
