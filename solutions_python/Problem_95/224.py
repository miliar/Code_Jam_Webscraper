from sys import stdin as I

#    abcdefghijklmnopqrstuvwxyz
r = '    o    u  l  rz n     a '

r = """
yeqz
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
"""
m = """
aozq
our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up
"""

def solve(s):
    rv = ''
    for c in s:
        rv += m[r.find(c)]
    return rv
    
def main():
    t = int(I.readline())
    for i in xrange(t):
        print "Case #%d: %s" % (i+1, solve(I.readline()[:-1]))
        
main()