import sys

def count(A, B):
    tested = [None] * (B-A+1)
    c = 0
    n = A
    while n < B:
        if tested[n-A]:
            n += 1
            continue
        astr = str(n) * 2
        nums = {n}
        l = len(astr) //2
        for i in xrange(1,l):
            if astr[i] == '0':
                continue
            m = int(astr[i:i+l])
            if m < A or m > B or m == n:
                continue
            if m < n:
                break
            nums.add(m)
            tested[m-A] = True
        else:
            x = len(nums)
            c += x*(x-1)//2
        n += 1
    return c

#print count(1, 9)
#print count(10, 40)
#print count(100, 500)
#print count(1111, 2222)
#print count(1000000, 2000000)
#print count(100000,  999999)

def main():
    f = open(sys.argv[1])
    out = open('result.txt', 'w')
    T = int(f.readline())
    
    for t in range(1, T+1):
        A, B = [int(c) for c in f.readline().split()]
        print>>out, "Case #%d: %d" % (t, count(A, B))

if __name__ == "__main__":
    main()