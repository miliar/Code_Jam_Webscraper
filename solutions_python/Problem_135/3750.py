t = input()
for i in range(t):
    b = []; d = [];
    a = input()
    for j in range(4):
        b.append([int(x) for x in raw_input().split()])
    c = input()
    for j in range(4):
        d.append([int(x) for x in raw_input().split()])

    row1 = b[a-1]; row2 = d[c-1];
    str2 = 'Case #'+ str(i+1) + ":"
    print str2, 
    if len(set(row1) & set(row2)) == 1:
        print list(set(row1) & set(row2))[0]
    if len(set(row1) & set(row2)) > 1:
        print 'Bad magician!'
    if len(set(row1) & set(row2)) == 0:
        print 'Volunteer cheated!'
