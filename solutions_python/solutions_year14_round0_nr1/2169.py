
for T in range(1, input()+1):
    r1 = input()
    cands = set()
    for i in range(1,5):
        row = [int(x) for x in raw_input().split()]
        if i == r1:
            cands = set(row)
    r2 = input()
    for i in range(1,5):
        row = [int(x) for x in raw_input().split()]
        if i == r2:
            new_cands = set(row)
            cands = cands & new_cands
    if len(cands) == 1:
        print "Case #" + str(T) + ": " + str(cands.pop())
    elif len(cands) == 0:
        print "Case #" + str(T) + ": Volunteer Cheated!"
    else:
        print "Case #" + str(T) + ": Bad magician!"