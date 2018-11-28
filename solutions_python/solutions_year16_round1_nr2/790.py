from base import cases
from collections import defaultdict

def solve(n):
    n = int(n)
    cant = defaultdict(int)
    for x in range(2*n-1):
        for num in raw_input().split(" "):
            cant[num]+=1
    imp = []
    for k, can in cant.iteritems():
        if can%2: imp.append(int(k))
    return " ".join(str(x) for x in sorted(imp))
    

if __name__ == "__main__":
    cases(solve)
