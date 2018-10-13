from collections import Counter

def score_(people, p):
    leftover = 0
    count = 0

    for x in people:
        if leftover == 0:
            count += 1

        leftover = (leftover + x) % p

    return count 


with open("A-small-attempt0.in") as infile:
    with open("A-small-attempt0.out", "w") as outfile:
        cases = int(next(infile))

        for case in range(1, cases+1):
            n, p = map(int, next(infile).split())
            groups = list(map(int, next(infile).split()))
            score = 0
           
            if p == 2:
                c = Counter([x%p for x in groups])
                score = c[0] + -(-c[1]//2)
            elif p == 3:
                c = Counter([x%p for x in groups])
                score += c[0]
                a, b = c[1], c[2]
                m = min(a, b)
                score += m
                a -= m
                b -= m
                score += -(-a // 3)
                score += -(-b // 3)

            print("Case #{}: {}".format(case, score), file=outfile)
