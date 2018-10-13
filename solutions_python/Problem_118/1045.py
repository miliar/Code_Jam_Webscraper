def palindromes(size, first=True):
    if first:
        if size == 1:
            yield 1
            yield 3
        elif size == 2:
            yield 11
        else:
            for p in palindromes(size - 2, False):
                yield int("1" + p + "1")
                
        if size % 2 == 0:
            yield int("2" + ("0" * (size - 2)) + "2")
        elif size != 1:
            s = "0" * ((size >> 1) - 1)
            yield int("2" + s + "1" + s + "2")
        else:
            yield 2
        
    else:
        if size == 1:
            yield "0"
            yield "1"
        elif size == 2:
            yield "00"
            yield "11"
        else:
            for p in palindromes(size - 2, False):
                yield "0" + p + "0"
                yield "1" + p + "1"
                
def up_to(limit):
    global l
    
    if limit == 0:
        return -1
    
    lo = 0
    hi = len(l) - 1
    
    while lo != hi:
        mid = ((lo + hi) >> 1) + (lo + hi) % 2
        
        if l[mid] <= limit:
            lo = mid
        else:
            hi = mid - 1
    
    return (lo + hi) >> 1

l = []
for n in range(1, 3):
    for i in palindromes(n):
        x = i*i
        xr = int(str(x)[::-1])
        
        if x == xr:
            l.append(x)

l.sort()

T = input()
for t in range(1, T + 1):
    A, B = map(int, raw_input().split())
    
    print "Case #%d: %d" % (t, up_to(B) - up_to(A - 1))


