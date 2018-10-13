inFile = open('C-small-2-attempt0.in')
outFile = open('C-small-2-attempt0.out', 'w')
testCases = int(inFile.readline())
caseNo = 1
while caseNo <= testCases:
    case = inFile.readline().split()
    stalls = int(case[0])
    people = int(case[1])
    gaps = [[stalls,1]]
    print('Case #%s: stall:%s people:%s\n' % (caseNo, stalls, people))
    while people > gaps[0][1]:
        if gaps[0][0]%2==1:
            if gaps[len(gaps)-1][0]==(gaps[0][0]-1)/2:
                gaps[len(gaps)-1][1]+=gaps[0][1]*2
            else:
                gaps.append([(gaps[0][0]-1)/2,gaps[0][1]*2]);
        else:
            if gaps[len(gaps)-1][0]==(gaps[0][0])/2:
                gaps[len(gaps)-1][1]+=gaps[0][1]
                gaps.append([(gaps[0][0])/2-1,gaps[0][1]]);
            else:
                gaps.append([(gaps[0][0])/2,gaps[0][1]]);
                gaps.append([(gaps[0][0])/2-1,gaps[0][1]]);
        people -= gaps[0][1]
        #print('split %s gaps of %s. people left: %s' % (gaps[0][1], gaps[0][0], people))
        gaps.pop(0)
    if gaps[0][0]%2==1:
        left = int((gaps[0][0]-1)/2)
        right = int((gaps[0][0]-1)/2)
    else:
        left = int((gaps[0][0])/2)
        right = int((gaps[0][0])/2 - 1)
    outFile.write('Case #%s: %s %s\n' % (caseNo, left, right))
    print('Case #%s: %s %s\n' % (caseNo, left, right))
    caseNo += 1
inFile.close()
outFile.close()