from pprint import pprint

num = input()

for testnum in range(num):
    d = []
    rows, cols = map(int,raw_input().split())
    for row in range(rows):
        d.append(map(int,raw_input().split()))

    possible = True
    while possible:
        possible = False
        for i in range(2):
            if d:
                current_min = min([min(r) for r in d])
            for row in reversed(d):
                if max(row)==current_min:
                    d.remove(row)
                    possible=True
            d=zip(*d)
                    
    print "Case #%i: %s" % (testnum+1, "YES" if d==[] else "NO")
