
def intersects(a1, b1, a2, b2):
    return (a1 > a2 and b2 > b1) or (a2 > a1 and b1 > b2)
    

f = open("c:/w.in")
f2 = open("c:/w.out", "w")
lines = map(lambda line: line.strip(), f.readlines())
test_count = int(lines.pop(0))

for i in range(test_count):
    count = 0

    n = int(lines.pop(0))
    heights = []
    for j in range(n):
        hs = map(int, lines.pop(0).split(" "))
        heights.append(hs)

    count = 0
    for i1 in range(n):
        for j1 in range(n):
            if i1 > j1:
                a1, b1 = heights[i1]
                a2, b2 = heights[j1]
                if intersects(a1, b1, a2, b2):
                    count += 1
        

    print heights
    print count
    answer = "Case #%d: %d\n" % (i + 1, count)
    f2.write(answer)

f2.close()
print "Done"



