_problem = 'B'

def se():
    problem_filename = _problem + '-example.in'
    output_filename = _problem + '-example.out'

    SolveFile(problem_filename, output_filename)

def SolveSmall():
    problem_filename = _problem + '-small-attempt1.in'
    output_filename = _problem + '-small.out'
    
    SolveFile(problem_filename, output_filename)

def SolveLarge():
    problem_filename = _problem + '-large.in'
    output_filename = _problem + '-large.out'
        
    SolveFile(problem_filename, output_filename)

def SolveFile(problem_filename, output_filename):
    problem_lines = []
    problem_file = open(problem_filename, 'r')

    for line in problem_file:
        problem_lines.append(line)

    problem_file.close()

    output_file = open(output_filename, 'w')

    print("Solving " + problem_filename)

    Solve(problem_lines, output_file)

    output_file.close()

def Solve(pl, output_file):
    print pl[0]
    definition = map(int,pl[0].split())

    N = definition[0]

    print "Problem definition " + str(definition)

    SolverInit(5)

    curline = 1

    for casenum in xrange(1,N+1):
        height, width = map(int,pl[curline].split())

        alts = []
        for row in pl[curline+1:curline+1+height]:
            alts.append(map(int,row.split()))

        curline = curline+1+height
            
        answer = str(SolveCase(alts))
        output_file.write("Case #%d: %s\n" % (casenum, answer))
        #print("Case #%d: %s" % (casenum, answer))

def SolverInit(initdata):
    pass

def SolveCase(alts):
    basinc = 0
    
    group = []
    direc = []
    counter = 0
    basins = []
    
    for y in xrange(len(alts)):
        row = alts[y]

        frow = []
        drow = []

        for x in xrange(len(row)):
            counter = counter + 1

            alt = alts[y][x]
            n,w,e,s = (20000,20000,20000,20000)
            if y-1>=0:
                n = alts[y-1][x]
            if x-1>=0:
                w = alts[y][x-1]
            if x+1<len(row):
                e = alts[y][x+1]
            if y+1<len(alts):
                s = alts[y+1][x]

            m = min(n,w,e,s)

            if alt<=m:
                #basin rename
                frow.append(basinc)
                basinc = basinc + 1
                drow.append( (x,y) )
                basins.append( (x,y) )
            else:
                frow.append(26+counter)
                ny = y
                nx = x
                if n == m:
                    ny = y-1
                elif w == m:
                    nx = x-1
                elif e == m:
                    nx = x+1
                elif s == m:
                    ny = y +1

                drow.append( (nx,ny) )

        direc.append(drow)
        group.append(frow)

    for bname in xrange(len(basins)):
        fillbasin(bname, basins[bname], group, direc)

    return "\n" + stringify(group)

_alpha = 'abcdefghijklmnopqrstuvwxyz????????????????????????????????????'

def stringify(groups):
    global _alpha
    count = 0
    remapstr = ['?']*26
    for y in xrange(len(groups)):
        for x in xrange(len(groups[0])):
            char = remapstr[groups[y][x]]
            if char == '?':
                remapstr[groups[y][x]] = _alpha[count]
                count = count + 1
                
    return "\n".join(map(lambda l: ' '.join(map(lambda x: remapstr[x],l)),groups))

def fillbasin(bname, pos, group, direc):
    for (dx,dy) in ( (-1,0), (1,0), (0,-1), (0,1)):
        ny = pos[1] + dy
        nx = pos[0] + dx
        if ny >=0 and nx >= 0 and ny < len(group) and nx < len(group[0]):
            if direc[ny][ nx] == pos:
                if group[ny][nx] != bname:
                    group[ny][nx] = bname                    
                    fillbasin(bname, (nx, ny), group, direc)
