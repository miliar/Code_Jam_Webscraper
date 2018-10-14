def solve(row1,row2):
    count = 0
    for e1 in row1:
        for e2 in row2:
            if e1==e2:
                count += 1
                ans = e1
    if count==1:
        return str(ans)
    if count==0:
        return "Volunteer cheated!"
    if count>1:
        return "Bad magician!"
    
f = open('A-small-attempt0.in', 'r')
line1 = f.readline()
cases = int(line1)
for case in range(1,cases+1):
    prob = []
    for l in range(10):
        line = f.readline()
        prob.append(line.split())
    sel1 = int(prob[0][0])
    row1 = prob[sel1]
    sel2 = int(prob[5][0])
    row2 = prob[sel2+5]
    print "Case #"+str(case)+ ": " + solve(row1,row2)

