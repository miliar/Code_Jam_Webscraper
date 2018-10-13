import itertools

def solve(S):
    for people_added in itertools.count():
        standing = people_added
        Sp = S[:]
        for i,n in enumerate(Sp):
            if i <= standing:
                standing += n
                Sp[i] = 0
            else:
                break
        else:
            return people_added


lines = open('input').readlines()[1:]
for i, line in enumerate(lines):
    S = list(map(int,line.split()[1]))
    s = solve(S)
    print("Case #%d:" % (i+1), s)