from sys import stdin

statuses = [
    'Game has not completed',
    'Draw',
    'X won',
    'O won'
]

checkDirections = [
    # horizontal checks
    ((0,0), (0,1)),
    ((1,0), (0,1)),
    ((2,0), (0,1)),
    ((3,0), (0,1)),

    # vertical checks
    ((0,0), (1,0)),
    ((0,1), (1,0)),
    ((0,2), (1,0)),
    ((0,3), (1,0)),

    # diagnoals
    ((0,0), (1,1)),
    ((3,0), (-1,1))
]

N = int(input())
for i in range(N):
    Xs = []
    Os = []
    nbPoints = 0
    for j in range(4):
        line = stdin.readline().strip()
        Xs.append(line.replace('T', 'X'))
        Os.append(line.replace('T', 'O'))
        nbPoints += line.count('.')

    # trash line
    stdin.readline()
    
    # status represents state of game
    # -1 : unfinished
    #  0 : draw 
    #  1 : X won
    #  2 : O won
    currStatus = statuses[0]

    for direction in checkDirections:
        pos = [
            direction[0][0],
            direction[0][1]
        ]

        XwinningDirection = True
        OwinningDirection = True
        for j in range(4):
            # print(pos, Xs[pos[0]][pos[1]], Os[pos[0]][pos[1]])

            if Xs[pos[0]][pos[1]] != 'X':
                XwinningDirection = False

            if Os[pos[0]][pos[1]] != 'O':
                OwinningDirection = False

            if not (XwinningDirection or OwinningDirection):
                break

            pos[0] += direction[1][0]
            pos[1] += direction[1][1]

        if XwinningDirection:
            currStatus = statuses[2]
            break

        if OwinningDirection:
            currStatus = statuses[3]
            break

    # it's a draw if there is no empty space
    if currStatus == statuses[0] and nbPoints == 0:
        currStatus = statuses[1]

    print('Case #{}: {}'.format(i+1, currStatus))


