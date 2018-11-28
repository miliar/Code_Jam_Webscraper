from collections import defaultdict

def solve(combine, opposed, invoke):
    #print (combine, opposed, invoke)
    elements = []
    for e in invoke:
        while elements:
            if e + elements[-1] in combine:
                e = combine[e + elements[-1]]
                elements.pop()
            else:
                break
        for f in elements:
            if f in opposed[e]:
                elements = []
                break
        else:
            elements.append(e)
    return "[" + ", ".join(elements) + "]"
    
def main():
    T = int(input())
    for i in range(1, 1 + T):
        line = iter(input().split())
        C = int(next(line))
        combine = {}
        for j in range(C):
            a, b, c = next(line)
            combine[a + b] = c
            combine[b + a] = c
        D = int(next(line))
        opposed = defaultdict(set)
        for j in range(D):
            a, b = next(line)
            opposed[a].add(b)
            opposed[b].add(a)
        N = int(next(line))
        invoke = next(line)
        ans = solve(combine, opposed, invoke)
        print("Case #%d: %s" % (i, ans))

if __name__ == "__main__":
    main()

