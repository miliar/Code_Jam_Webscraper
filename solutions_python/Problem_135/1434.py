numTests = int(raw_input())
for i in xrange(numTests):
    first = int(raw_input())
    L = []
    for j in xrange(4):
        L.append(raw_input().strip().split())
    s1 = set(L[first - 1])
    second = int(raw_input())
    L = []
    for j in xrange(4):
        L.append(raw_input().strip().split())
    s2 = set(L[second - 1])
    s3 = s1.intersection(s2)
    output = "Case #" + str(i + 1) + ": "
    if len(s3) == 0:
        output += "Volunteer cheated!"
    elif len(s3) == 1:
        output += s3.pop()
    else:
        output += "Bad magician!"
    print output
