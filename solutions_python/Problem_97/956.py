import sys

def count(A, B):
    used = set()
    ans = 0
    for i in range(A, B+1):
        d2 = str(i)
        for t in range(len(str(d2))):
            d2 = str(d2)
            d2 = int(d2[-1] + d2[:-1])
            if d2 != i and (d2, i) not in used and (i, d2) not in used:
                if d2 <= B and d2 >= A:
                    ans += 1
                    used.add((d2,i))
    return ans

inp = sys.argv[1]
out = sys.argv[2]

with open(inp, 'r') as f:
    lines = [[int(i) for i in l.split()] for l in f.readlines()[1:]]
    counter = 1
    for l in lines:
        with open(out, 'a') as output:
            output.write('Case #{0}: {1}\n'.format(counter, count(l[0], l[1])))
            counter += 1


