import os, sys
import json


def make_dict():
    s = """ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv"""
    o = """our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up"""
    d = {}
    for i in range(len(s)):
        d[s[i]] = o[i]
    f = open('A_dict.json', 'w')
    f.write(json.dumps(d))
    f.close()

d = {}
def read_dict():
    global d
    f = open('A_dict.json')
    d = json.load(f)
    f.close()


def conv(s):
    r = "".join(map(lambda x: d[x], s))
    return r
            
def solve():
    ls = sys.stdin.readlines()
    n = int(ls[0])
    for i in range(n):
        print "Case #%d: %s" % (i+1, conv(ls[i+1]))     
    
    
if __name__ == '__main__':
    make_dict()
    read_dict()
    d['z']='q'
    d['q']='z'
    d['\n'] = ''
    solve()
