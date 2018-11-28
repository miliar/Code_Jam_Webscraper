def solve(f) :
    a, b, k = f.readline().split()
    a = int(a)
    b = int(b)
    k = int(k)
    count = 0
    for i in range(a) :
        for j in range(b) :
            if i&j < k :
                count += 1
    

    return count

if __name__ == '__main__' :
    with open('B-small-attempt0.in') as f:
        t = int(f.readline())
        for i in range(t) :
            print ('Case #{0}: {1}'.format(i + 1, solve(f)))
