import sys;


def solve(n):
    d = list(map(int, str(n)));
    idxLastIncreasing,prevVal = 0,0;
    dec = False;
    for i in range(0, len(d)):
        if d[i]>prevVal:
            idxLastIncreasing = i;
        if d[i]<prevVal:
            dec = True;
            break;
        prevVal=d[i];
    if dec:
        d[idxLastIncreasing] -= 1;
        d[idxLastIncreasing+1:] = [9]*(len(d)-(idxLastIncreasing+1))
    return int("".join(map(str,d)))

f = sys.stdin

cases = f.readline()
for case in range(1,int(cases)+1):
    n = f.readline().strip()
    sol = solve(n)
    print ("Case #{}: {}".format(case,sol));


