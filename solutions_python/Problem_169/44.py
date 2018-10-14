def solve(V,X,r1,c1,r2,c2):
    if c1 < X > c2:
        return "IMPOSSIBLE"

    elif c1 > X < c2:
        return "IMPOSSIBLE"

    if c1 == c2:
        if c1 != X or c2 != X:
            return "IMPOSSIBLE"

        return V/(r1+r2)

    if c1 == X and c2 != X:
        return V/r1

    if c2 == X and c1 != X:
        return V/r2

    d = r1*r2*c2 - r1*r2*c1
    t1 = (r2*c2*V - r2*V*X)/d
    t2 = (-r1*c1*V + r1*V*X)/d

    return max(t1, t2)

    

with open("B.out", "w") as outfile:
    with open("B-small-attempt2.in") as infile:
        ncases = int(next(infile))

        for case in range(1, ncases + 1):
            N,V,X = map(float, next(infile).split())

            if N == 2:
                r1,c1 = map(float, next(infile).split())
                r2,c2 = map(float, next(infile).split())

                print("Case #{}: {}".format(case, solve(V,X,r1,c1,r2,c2)), file=outfile)

            else:
                r1,c1 = map(float, next(infile).split())
            
                if c1 == X:
                    print("Case #{}: {}".format(case, V/r1), file=outfile)

                else:
                    print("Case #{}: IMPOSSIBLE".format(case), file=outfile)
