fin = open("C-small-attempt2.in", "r")
fout = open("smallc.out", "w")


def next():
    return fin.readline().strip()
    
def isqrt(n):
    x = n
    y = (x + n // x) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x
    
def palen(a):
    front = a[: len(a) // 2]
    if len(a) % 2:
        back = a[len(a) // 2 + 1 :]
    else:
        back = a[len(a) // 2 :]

    back = back[::-1]

    return front == back
    
for case in xrange(1, int(next()) + 1):
    fout.write("Case #" + str(case) + ": ")

    low, high = map( int, next().split(" ") )
    
    sLow = isqrt(low)
    if not ((sLow ** 2) == low):
        sLow += 1
        
    sHigh = isqrt(high)
    
    count = 0
    
    print sLow, " " , sHigh
    
    for i in xrange(sLow, sHigh + 1):
        if palen(str(i)):
            if palen(str(i ** 2)):
                count += 1
    
    fout.write(str(count))
    
    fout.write('\n')
fin.close()
fout.close()