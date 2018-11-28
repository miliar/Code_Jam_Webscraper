__author__ = 'knusper'
import math
import sys

def readint(ip):
    return int(ip.readline())
def readintlist(ip):
    return list(map(int,ip.readline().split()))
def readintset(ip):
    return set(map(int,ip.readline().split()))
def readfloat(ip):
    return float(ip.readline())
def readfloatlist(input):
    return list(map(float,ip.readline().split()))
def readstring(ip):
    return ip.readline().strip()
def writeanswer(op,t,sol):
    op.write("Case #"+str(t)+": "+str(sol)+"\n")

fn="A-large"

ip = open(fn+".in", 'r')
op = open(fn+".out", "w")

for t in range(1,readint(ip)+1):
    N=readint(ip)
    m=readintlist(ip)
    y=0
    z=0
    rate=0
    for x in range(N-1):
        if m[x+1]<m[x]:
            y+=m[x]-m[x+1]
        if m[x]-m[x+1]>rate:
            rate=m[x]-m[x+1]
    for x in range(N-1):
        z+=min(rate,m[x])
    sol=str(y)+" "+str(z)
    writeanswer(op,t,sol)
op.close()