import sys, re, string

CACHE={}

def remove_non_needle_char(haystack, needle):
    r=[]
    for c in haystack:
        if c in needle:
            r.append(c)     
    return ''.join(r).strip()

def sum(haystack, needle):
    haystack=remove_non_needle_char(haystack, needle)
    return _sum(haystack, needle, 0)

def _sum(haystack, needle, depth):
    if CACHE.has_key((haystack, needle)):
        return CACHE[(haystack, needle)]
    if not haystack:
        return 0
    elif haystack==needle:
        return 1
    elif len(needle)==1:
        return haystack.count(needle)
    else:
        cnt=0
        i=0
        while True:
            i=haystack.find(needle[0], i)
            if i==-1:
                break
            #print depth, len(haystack), len(needle), i
            cnt=(cnt+_sum(haystack[i+1:], needle[1:], depth+1))%10000
            i+=1
        CACHE[(haystack, needle)]=cnt
        return cnt 

def read_n():
    return int(sys.stdin.readline())

if __name__=='__main__':
    n=read_n()
    for i in range(n):
        print 'Case #%d: %04d' % (i+1, sum(sys.stdin.readline().strip(), 'welcome to code jam'))
