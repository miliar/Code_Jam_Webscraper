def solve2(n, k):
    i = 1
    while k - i > 0:
        k -= i
        n -= i
        i *= 2

    n -= i
    l = n//(2*i)
    r = n//(2*i)

    remainder = n%(2*i)
    if remainder >= k:
        l += 1
    if remainder >= k+i:
        r += 1

    return l, r


with open("C-large.in") as infile:
    with open("C-large.out", "w") as outfile:
        cases = int(next(infile))

        for i in range(1, cases+1):
            n, k = map(int, next(infile).split())
            print("Case #{}: {} {}".format(i, *solve2(n, k)), file=outfile)
                
            
