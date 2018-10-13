import sys

def tidy(N):
    x = [int(i) for i in str(N)]
    return x == sorted(x)


def find_increasing(l):
    if len(l) == 1:
        return True, None
    
    i = 0
    first_inc = None
    length = len(l)
    while i < length - 1 and l[i] <= l[i+1]:
        if first_inc is None and l[i] < l[i+1]:
            first_inc = i + 1
        i += 1
    if first_inc is None:
        first_inc = 0
        
    return i == length - 1, first_inc


def last_tidy(N):
    Nl = [int(x) for x in str(N)]

    a, b = find_increasing(Nl)
    if a:
        return N
    else:
        Nl[b] -= 1
        for i in range(b+1, len(Nl)):
            Nl[i] = 9
        new_N = int("".join(str(x) for x in Nl))
        return new_N

with open(sys.argv[1]) as f, open(sys.argv[2], "w") as out:
    T = next(f)

    for i, line in enumerate(f, start=1):
        answer = last_tidy(int(line))
        print(f"Case #{i}: {answer}", file=out)