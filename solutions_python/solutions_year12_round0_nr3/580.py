debug = True
debug = False

t = int(raw_input())
cache = set()

for i in range(t):
    row = raw_input().split(" ")
    
    a = int(row[0])
    b = int(row[1])

    result = set()
    
    for n in range(a, b + 1):
        strn = str(n)
        str2n = strn * 2
        
        for j in range(1, len(strn)):
            recycled = int(str2n[j:j + len(strn)])
            
            if recycled == n: continue
            
            if a <= recycled <= b:
                pair = (min((recycled, n)), max((recycled, n)))
                if pair not in result:
                    result.add(pair)
                    if debug: print "%d %d" % pair

    print "Case #%d: %d" % (i + 1, len(result))
