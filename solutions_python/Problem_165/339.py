from math import ceil

def solve(C,W):
    to_eliminate = C - W
    num_hits = int(ceil(to_eliminate / float(W)))
    return num_hits + W

if __name__ == "__main__":
    T = int(raw_input())
    for i in range(1, T+1):
        R,C,W = map(int, raw_input().split())
        print "Case #%d: %d" % (i, solve(C,W))
    
    
