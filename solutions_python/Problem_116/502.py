from itertools import chain

def status(cube):
    a=(cube[0],cube[6],cube[12],cube[18])
    b=(cube[3],cube[7],cube[11],cube[15])
    lines=cube.split('\n')
    for line in chain((a,b),lines,zip(*lines)):
        if ('.' not in line)and(line.count('T')<2):
            if 'X' not in line:
                return "O won"
            if 'O' not in line:
                return "X won"
    if '.' in cube:
        return "Game has not completed"
    return "Draw"

file=open(r"C:\Users\user\Downloads\A-large.in").read().split('\n',1)[1]
cubes=file.split('\n\n')

for i, cube in enumerate(cubes):
    print("Case #"+str(i+1)+":", status(cube))

