GABRIEL = "GABRIEL"
RICHARD = "RICHARD"

def f(X, R, C):
    return (
        f(X, C, R) if R > C else GABRIEL if (
            True if X == 1 else
            (R * C) % 2 == 0 if X == 2 else
            (R,C) in ((3,3), (3,4), (2,3)) if X == 3 else
            not(R < 4 and C < 4 or R <= 2) if X == 4 else "?"
        ) else RICHARD
    )

def parse(filename):
    it = iter(open(filename))
    N = int(next(it))
    for i in range(N):
        print("Case #{}: {}".format(i+1, f(*map(int, next(it).split()))))
        
parse("D-small-attempt0.in")