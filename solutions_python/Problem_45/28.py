def find_seg(num, segs):
    for seg in segs:
        if num < seg[0] or num > seg[1]:
            continue
        return seg
    print "WTF", num, segs
    
def min_num(l, segs):
    if len(l) == 1:
        seg = find_seg(list(l)[0], segs)
        return seg[1] - seg[0]
    
    ans = None
    for pris in l.copy():
        seg = find_seg(pris, segs)
        segs.remove(seg)
        a, b = seg
        a = (a, pris-1)
        b = (pris+1, b)
        segs.add(a)
        segs.add(b)
        l.remove(pris)
        tmp = min_num(l, segs)
        tmp += seg[1] - seg[0]
        if ans is None or tmp < ans:
            ans = tmp

        segs.remove(a)
        segs.remove(b)
        l.add(pris)
        segs.add(seg)
        
    return ans

def main():
    N = int(raw_input())
    for i in range(1, N+1):
        P, Q = map(int, raw_input().split())
        l = set(map(int, raw_input().split()))
        segs = set([(1, P)])
        ans = min_num(l, segs)
        print "Case #%d: %d" % (i, ans)
        
if __name__ == "__main__":
    main()
