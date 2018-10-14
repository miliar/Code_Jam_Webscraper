import re

def process_case() :
    N, M = map(int, raw_input().split())
    exist = []
    new = []
    for i in range(N) :
        exist.append( raw_input() )
    for i in range(M) :
        new.append( raw_input() )
    # print exist, new

    tree = {} 
    for p in exist :
        p = p[1:]
        sp = p.split("/")
        curr = tree
        for fn in sp :
            if not fn in curr :
                curr[fn] = {}
            curr = curr[fn]
    count = 0
    for p in new :
        p = p[1:]
        sp = p.split("/")
        curr = tree
        for fn in sp :
            if not fn in curr :
                curr[fn] = {}
                count += 1
            curr = curr[fn]
        
    return "%d" % count


if __name__ == "__main__" :
    case_num = int(raw_input())
    for i in range(case_num) :
        result = process_case()
        print "Case #%d: %s" % (i+1, result)
