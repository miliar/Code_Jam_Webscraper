def judge():
    pass

for i in range(int(raw_input())):
    pos1 = int(raw_input())
    for j in range(4):
        line = raw_input()
        if j + 1 == pos1:
            cand1 = set(line.split())
    pos2 = int(raw_input())
    for j in range(4):
        line = raw_input()
        if j + 1 == pos2:
            cand2 = set(line.split())
    inter = cand1.intersection(cand2)
    if len(inter) == 1:
        print('Case #%s: %s' % (i + 1, inter.pop()))
    elif len(inter) > 1:
        print('Case #%s: Bad magician!' % (i + 1))
    else:
        print('Case #%s: Volunteer cheated!' % (i + 1))
