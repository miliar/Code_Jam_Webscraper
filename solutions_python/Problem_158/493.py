cases = []
with open('D-small-attempt1.in') as f:
    n = int(f.readline())
    for i,line in enumerate(f):
        x,r,c = [int(s) for s in line.split()]
        if x == 1 :
            safe = True
        elif x == 2 :
            safe = (r*c)%2 == 0
        elif x == 3 :
            safe = (r*c)%3 == 0 and r*c > 3
        else :
            safe = (r*c == 16 or r*c == 12)
        
        if safe:
            winner = 'GABRIEL'
        else:
            winner = 'RICHARD'
        cases.append('Case #'+str(i+1)+': '+winner+'\n')

with open('D-small-attempt1.out','w+') as g:
    g.writelines(cases)