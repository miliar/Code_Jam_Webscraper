import sys

def maxsum(l):
    l.sort(reverse=True)
    ans = sum(l[:-1])
    return ans

def do_candy(s,ctr):
    l = s.split()
    l = map(int,l)
    r = 0
    for t in l:
        r = r ^ t
    if r != 0:
        ans = -1
        print "Case #%s: NO" % (ctr)
    else:
        ans = maxsum(l)
        print "Case #%s: %s" % (ctr,ans) 

if __name__ == "__main__":
    f = open(sys.argv[1])
    n = int(f.readline())
    for i in range(0,n):
        s = f.readline()
        s = f.readline().strip()
        #if s[0] == '#':
        #    continue
        do_candy(s,i+1)
    f.close()
