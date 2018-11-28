from sys import stdin

m = int(stdin.readline().strip())
for _ in xrange(m):
    string = stdin.readline().strip()
    map = {}
    base = max(len(set(string)),2)
    map[string[0]] = 1
    num = 0
    for c in string:
        if not c in map:
            if len(map) == 1:
                map[c] = 0
            else:
                map[c] = len(map)
        num = num * base + map[c]
    print "Case #%d: %d"%(_+1,num)
    
