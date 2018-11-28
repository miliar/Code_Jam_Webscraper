def recycle(n):
    n = n[-1] + n[:-1]
    return n

def solve(A, B):
    l = len(str(B))
    t = 0
    distinct = {}
    for x in range(A, B+1):
        n = str(x)
        for y in range(l-1):
            n = recycle(n)
            if x < int(n) <= B:
                if (x,int(n)) not in distinct:
                    distinct[(x,int(n))] = True
                    t += 1
    return t

fin = file('C-large.in', 'r')
fout = file('file.out', 'w')
count = int(fin.readline())
for c in range(count):
    A, B = map(int, fin.readline().strip('\n').split())
    solution = solve(A,B)
    fout.write('Case #%d: %s\n' % (c+1, solution))
        