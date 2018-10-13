for case in range(1, int(input())+1):
    (N, K) = map(int,input().split())
    d = {N:1}
    space = max(d.keys())
    while K > d[space]:
        placed = d.pop(space)
        d[space//2] = d.get(space//2,0) + placed
        d[(space-1)//2] = d.get((space-1)//2,0) + placed
        K -= placed
        space = max(d.keys())
    print ("Case #%d: %s %s" % (case,space//2,(space-1)//2))
