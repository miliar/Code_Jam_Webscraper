'''
Created on 10 apr. 2015

Infinite Pancakes

@author: Kristian Slabbekoorn
'''

lines = [line.strip() for line in open('inD.txt')]
out = open('./outD.txt', 'w+')
case = 0
for i in range(1, int(lines[0])+1):
    case += 1
    
    D = lines[i]
    X,R,C = map(int, lines[i].split())

    size = R*C
    winner = "GABRIEL"
    
    if size % X != 0 or (X/2 + X%2) > min([R,C]) or X > max([R, C]) or (X > 3 and (X/2 + 1) > min([R,C])) or X >= 7:
        winner = "RICHARD"
    
        

    out.write("Case #" + str(case) + ": " + str(winner) + "\n")
out.close()