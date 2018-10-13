# -------------------------
# Google Code Jam 2017
# Round 1A
# 2017 April 14
# Brendan Wood
# brendanwood1989@gmail.com
# -------------------------
filename = 'A-large'


def solve(R,C,cake):

    iced = dict()

    blank = []

    for row in range(R):
        
        icedrow = ''
        
        if cake[row] == '?'*C:
            blank.append(row)
            continue
        
        for square in cake[row]:
            last = square
            if last != '?':
                break
        
        for square in cake[row]:
            if square == '?':
                icedrow += last
            else:
                icedrow += square
                last = square
        
        iced[row] = icedrow
    
    last = iced[min(iced.keys())]
    for row in range(R):
        if row in iced:
            last = iced[row]
        else:
            iced[row] = last
                
    return iced
    
with open(filename+'.in') as f:
    data = f.read().splitlines()

f = open(filename+'.out', 'w')

T = int(data.pop(0))

for case in range(T):
    R,C = map(int,data.pop(0).split())
    cake = []
    for row in range(R):
        cake.append(data.pop(0))
    iced = solve(R,C,cake)
    
    f.write('Case #{}:\n'.format(case+1))
    for row in range(R):
        f.write(iced[row] + '\n')
        
f.close()