import string, sys

input = file(sys.argv[1]).readline

output = open('out.txt', 'w')

for case in range(int(input())):
    winner = "GABRIEL"
    values = [int(x) for x in input().split()]
    if ((values[1]*values[2])%values[0])>0:
        winner = "RICHARD"
    if values[0]>6:
        winner = "RICHARD"
    smalldim = values[1]
    if values[2]<smalldim:
        smalldim=values[2]
    if (values[0]+1)/2>smalldim:
        winner = "RICHARD"
    if (values[0]+1)/2==smalldim:
        if values[0]>3:
            winner = "RICHARD"
    output.write("Case #" + str(case+1) + ": " + winner + "\n")