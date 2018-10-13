'''
Created on Apr 12, 2013

@author: ericdennison
'''



runs = [(0,1,2,3),
        (4,5,6,7),
        (8,9,10,11),
        (12,13,14,15),
        (0,4,8,12),
        (1,5,9,13),
        (2,6,10,14),
        (3,7,11,15),
        (3,6,9,12),
        (0,5,10,15)]

def win(c,l):
    v = ['T',c]
    for r in runs:
        if l[r[0]] in v and l[r[1]] in v and l[r[2]] in v and l[r[3]] in v:
            return True
    return False
            
    

def evaluate(f,l):
    ll = []
    for i in range(0,4):
        ll += list(l[i].strip())
    # check for wins
    if win('X',ll):
        f.write( "X won")
    elif win('O',ll):
        f.write("O won")
    elif '.' in ll:
        f.write("Game has not completed")
    else:
        f.write("Draw")

f = file("A-large.in").readlines()
#f = file("data.txt").readlines()
fo = file("output.txt",'w')
n = int(f[0])
for i in range(0,n):
    if i != 0:
        fo.write('\n')
    fo.write("Case #{0}: ".format(i+1))
    evaluate(fo,f[(i*5)+1:])
fo.close()        