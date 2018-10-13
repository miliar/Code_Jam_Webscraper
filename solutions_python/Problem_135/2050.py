def magic_trick(rows1, a1, rows2, a2):
    pos = set()
    result = []
    for n in rows1[a1-1]:
        pos.add(n)

    for n in rows2[a2-1]:
        if n in pos:
            result.append(n)

    if len(result)>1:
        return "Bad magician!"
    elif len(result)==1:
        return result[0]
    else:
        return "Volunteer cheated!"


T=int(raw_input())
solutions = []
for t in xrange(T):
    a1 = int(raw_input())
    rows1 = []
    for r in xrange(4):
        rows1.append(raw_input().strip().split())
    a2 = int(raw_input())
    rows2 = []
    for r in xrange(4):
        rows2.append(raw_input().strip().split())
    sol = magic_trick(rows1,a1,rows2,a2)
    form = "Case #%d: %s" %(t+1, sol)
    solutions.append(form)

with open('magic_output.txt', 'w') as f:
    for s in solutions[:-1]:
        f.write(s)
        f.write("\n")
    f.write(solutions[-1])

    