t = int(input())
for i in range (1, t+1):
    finaloutput = ''
    first = int(input()) - 1
    row = []
    srow = []
    for j in range(4):
        insert = input().split()
        row.append(insert)
    second = int(input())-1
    for j in range(4):
        insert = input().split()
        srow.append(insert)
    # test for volunteer cheating
    cheating = True
    for j in row[first]:
        if j in srow[second]:
            cheating = False
    if cheating:
        finaloutput = 'Volunteer cheated!'
    # test for repetition
    repeats = 0
    for a in list(row[first]):
        for b in list(srow[second]):	
        	if a == b:
        		repeats += 1
    if repeats > 1:
        finaloutput = 'Bad magician!'
    else:
        for j in row[first]:
            if j in srow[second]:
                finaloutput = j
    print('Case #{0}: {1}'.format(i, finaloutput))
    
