import sys

f = open('D:\Users\john\My Documents\Google Code Jam 2014\magic_small.txt','r+')
g = open('D:\Users\john\My Documents\Google Code Jam 2014\magic_small_answer.txt','w+')

tricks = int(f.readline())
print(tricks)

for t in range(tricks):
    grid1 = []
    grid2 = []
    answers = []
    
    guess1 = f.readline()
    grid1.append(f.readline().split())
    grid1.append(f.readline().split())
    grid1.append(f.readline().split())
    grid1.append(f.readline().split())
    
    guess2 = f.readline()
    grid2.append(f.readline().split())
    grid2.append(f.readline().split())
    grid2.append(f.readline().split())
    grid2.append(f.readline().split())
    
    g.write('Case #'+str(t+1)+' : ')
    match = False
    bad = False
    found = 0
    for x in grid1[int(guess1)-1]:
        for y in grid2[int(guess2)-1]:
            if x == y and match:
                g.write('Bad magician!\n')
                match = False
                bad = True
                break
            elif x == y:
                match = True
                found = x
        if bad:
            break
    if match:
        g.write(found+'\n')
    elif found == 0:
        g.write('Volunteer cheated!\n')
        
f.close()
g.close()