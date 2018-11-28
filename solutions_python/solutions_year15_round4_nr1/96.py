# Import the file
in_file = 'A-large.in'
Type = 'small' if in_file.count('small') > 0 else 'large' if in_file.count('large') > 0 else 'test'
out_file = 'A-{0}.out'.format(Type)

with open(in_file,'r') as f:
    data = f.readlines()

data2 = data.copy()
# Format the data
Tt = int(data[0])
del data[0]
    
OUT = []
for k in range(Tt):
    # Enter code here
    R,C = list(map(int,data[0].split(' ')))
    del data[0]
    Pegs = {}
    # Import the data
    for r in range(R):
        for c,val in enumerate(data[r][:-1]):
            Pegs[r,c] = val
    # Check for errors, i.e. cells which push over edges
    Broken = []
    for cell in Pegs:
        if Pegs[cell] == '.':
            continue
        if Pegs[cell] == 'v':
            # Keep going down
            r = 1
            FLAG = False
            while r+cell[0] < R:
                if Pegs[(cell[0]+r,cell[1])] != '.':
                    FLAG = True
                    break
                r += 1
            if not FLAG: Broken.append(cell)
        if Pegs[cell] == '^':
            # Keep going up
            r = 1
            FLAG = False
            while cell[0]-r >= 0:
                if Pegs[(cell[0]-r,cell[1])] != '.':
                    FLAG = True
                    break
                r += 1
            if not FLAG: Broken.append(cell)
        if Pegs[cell] == '>':
            # Keep going left
            r = 1
            FLAG = False
            while r+cell[1] < C:
                if Pegs[(cell[0],cell[1]+r)] != '.':
                    FLAG = True
                    break
                r += 1
            if not FLAG: Broken.append(cell)
        if Pegs[cell] == '<':
            # Keep going right
            r = 1
            FLAG = False
            while cell[1]-r >= 0:
                if Pegs[(cell[0],cell[1]-r)] != '.':
                    FLAG = True
                    break
                r += 1
            if not FLAG: Broken.append(cell)
    if len(Broken) == 0:
        OUT.append(0)
        del data[:R]
        continue
    Poss = [False]*len(Broken)
    for dir in ('<','>','^','v'):
        for i,cell in enumerate(Broken):
            Pegs[cell] = dir
            if Pegs[cell] == 'v':
                # Keep going down
                r = 1
                FLAG = False
                while r+cell[0] < R:
                    if Pegs[(cell[0]+r,cell[1])] != '.':
                        FLAG = True
                        break
                    r += 1
                if FLAG: Poss[i] = True
            if Pegs[cell] == '^':
                # Keep going up
                r = 1
                FLAG = False
                while cell[0]-r >= 0:
                    if Pegs[(cell[0]-r,cell[1])] != '.':
                        FLAG = True
                        break
                    r += 1
                if FLAG: Poss[i] = True
            if Pegs[cell] == '>':
                # Keep going left
                r = 1
                FLAG = False
                while r+cell[1] < C:
                    if Pegs[(cell[0],cell[1]+r)] != '.':
                        FLAG = True
                        break
                    r += 1
                if FLAG: Poss[i] = True # Broken.append(cell)
            if Pegs[cell] == '<':
                # Keep going right
                r = 1
                FLAG = False
                while cell[1]-r >= 0:
                    if Pegs[(cell[0],cell[1]-r)] != '.':
                        FLAG = True
                        break
                    r += 1
                if FLAG: Poss[i] = True #Broken.append(cell)
    del data[:R]
    if all(Poss): OUT.append(len(Poss))
    else: OUT.append('IMPOSSIBLE')
    pass
        

with open(out_file,'w') as f:
    for i in range(Tt):
        f.write('Case #{0}: {1}\n'.format(i+1,OUT[i]))
