import fractions

def distances(l):
    l = l[:]
    for i in range(len(l)-1):
        l[i] = l[i+1] - l[i]
    l.pop()
    return l

def gcd(l):
    return reduce(fractions.gcd, l)

if __name__ == "__main__":
    n = int(raw_input())
    for i in range(1, n+1):
        numbers = map(int, raw_input().split())[1:]
        numbers.sort()
        T = gcd(distances(numbers))
        y = (T - numbers[0] % T) % T
        print "Case #%d: %d" % (i, y)
        
        
