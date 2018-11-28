'''
Created on May 7, 2010

@author: john
'''
fname=r"c:\Users\john\Downloads\A-large"
fin = open(fname+".in")
fout = open(fname+".out","w")
T=int(fin.readline())
OUT = ["OFF","ON"]
for i in range(T):
    N,K = map(int, fin.readline().split(" "))
    fout.write( "Case #%d: %s\n" % (i+1, OUT[reduce(lambda a,b: K>>b&a, range(N), 1)]))
