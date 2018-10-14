from fractions import gcd
from itertools import izip


def intersect_count(pairs):
    ret = 0
    for pos,pivot in enumerate(pairs):
        for det in pairs[pos:]:
            ret += 1 if pivot[0] < det[0] and pivot[1] > det[1] else 0
            ret += 1 if pivot[0] > det[0] and pivot[1] < det[1] else 0
    return ret

def print_res(caseno,res):
    print "Case #%d: %s" %(caseno,res) 

def main():
    for case in xrange(1,int(raw_input())+1):
        N = [long(w) for w in raw_input().split(' ')][0]
        pairs = []
        for i in range(N):
            pairs.append(tuple([long(w) for w in raw_input().split(' ')]))
        print_res(case,intersect_count(pairs))

if __name__=="__main__":
    main()
