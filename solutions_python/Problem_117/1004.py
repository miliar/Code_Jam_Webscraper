fInput = open("B-large.in", 'r')
fOutput = open("B-large.out", 'w')

num_cases = int(fInput.next())

for case in range(1,num_cases+1):
    if case%((num_cases/10) if num_cases>=10 else 1)==0: print '.',
    height, width = map(int, fInput.next().split())
    lawn = []
    for row in range(height):
        lawn.append(map(int, fInput.next().split()))
    out_str = "YES"
    for rowId, row in enumerate(lawn):
        maxRow = max(row)
        nonMaxPosList = filter(lambda i:row[i]<maxRow, range(width))
        for colId in nonMaxPosList:
            col = [x[colId] for x in lawn]
            if max(col) > lawn[rowId][colId]: out_str = "NO"
    fOutput.write("Case #{0}: ".format(case) + out_str + "\n")
    
fInput.close()
fOutput.close()
print "\t[DONE]"