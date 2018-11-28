import sys

def solve(caseNum, cake, m , n):
    print "Case #{}:".format(caseNum)
    cake = assign(cake, m, n)
    for i in range(m):
        print ''.join(cake[i])


def assign(cake, m, n):
    assignment = [[] for _ in range(26)] # [(sr, sc), (er, ec)]
    unAssigned = set() # unAssigned: [(r, c)]
    base = ord('A')
    for i in range(m):
        for j in range(n):
            if cake[i][j] == '?':
                cake[i][j] = -1
            else:
                cake[i][j] = ord(cake[i][j]) - base
    for cr in range(m):
        for cc in range(n):
            if cake[cr][cc] >= 0:
                assignment[cake[cr][cc]] = [(cr, cc), (cr, cc)]
            else:
                unAssigned.add((cr, cc))

    def dfs():
        # curr = None
        # print "===="
        # print cake
        # print unAssigned
        currs = []
        for cr, cc in unAssigned:
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0,-1)]:
                if  cr+dr >= 0 and cr+dr < m and cc + dc >= 0 and cc + dc < n and cake[cr+dr][cc + dc] >= 0 :
                    currs.append((cr, cc))
        if not currs:
            return True
        for curr in currs:
            (cr, cc) = curr
            candidates = []
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0,-1)]:
                if  cr+dr < 0 or cr+dr >= m or cc + dc < 0 or cc + dc >= n or cake[cr+dr][cc + dc] < 0 : continue
                candidates.append(cake[cr+dr][cc + dc])
            # print candidates
            for c in candidates:
                leftUpper, rightLower = assignment[c]
                row_expandable = (leftUpper[1]-cc)*(rightLower[1]-cc)<=0
                if row_expandable:
                    if max(cake[cr][leftUpper[1]:rightLower[1]+1]) < 0:
                        for j in range(leftUpper[1],rightLower[1]+1):
                            unAssigned.remove((cr, j))
                            cake[cr][j] = c
                        old = assignment[c]
                        assignment[c] = [(min(old[0][0], cr), old[0][1]), (max(old[1][0], cr), old[1][1])]
                        if dfs(): return True
                        assignment[c] = old
                        for j in range(leftUpper[1],rightLower[1]+1):
                            unAssigned.add((cr, j))
                            cake[cr][j] = -1

                else:
                    col_expandale = True
                    for i in range(leftUpper[0], rightLower[0]+1):
                        if cake[i][cc] >=0:
                            col_expandale = False
                            break
                    if col_expandale:
                        for i in range(leftUpper[0], rightLower[0]+1):
                            unAssigned.remove((i, cc))
                            cake[i][cc] = c
                        old = assignment[c]
                        assignment[c] = [(old[0][0], min(cc,old[0][1])), (old[1][0], max(cc, old[1][1]))]
                        if dfs(): return True
                        assignment[c] = old
                        for i in range(leftUpper[0], rightLower[0]+1):
                            unAssigned.add((i, cc))
                            cake[i][cc] = -1
        return False
    dfs()
    for i in range(m):
        for j in range(n):
            cake[i][j] = chr(cake[i][j] + base)
    return cake





lines = [line for line in sys.stdin]
t = int(lines[0])
caseNum = 1
curr = 1
for k in range(t):
    line = lines[curr]
    m, n = [int(x) for x in line.split()]
    curr +=1
    cake = []
    for r in range(m):
        cake.append([x for x in lines[curr].rstrip('\n')])
        curr += 1
    solve(k+1, cake, m, n)
